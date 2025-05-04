"""
@file controller.py
@package controller
@brief Balík implementujúci lexikálnu analýzu, syntaktickú analýzu, výpočet výrazov.

======== Copyright (c) 2023, FIT VUT Brno, All rights reserved. ============

Purpose:     IVS 2nd project - package desc

$NoKeywords: $ivs_project_2 $controller.py
@author     Jakub Kasem <xkasem02@stud.fit.vutbr.cz>
@author Martin Mores <xmores02@stud.fit.vutbr.cz>
$Date:       $2023-03-13
============================================================================
"""
import mathLib as ml
 
class Token:
    """@brief Reprezentácia časti výrazu.
    """
    def __init__(self, token_type, value):
        """@brief Vytvorenie inštancie triedy.

        Args:
            @param token_type (str): typ tokenu ako reťazec
            @param (str): hodnota tokenu ako reťazec
        """
        self.token_type = token_type
        self.value = value

class Lexer:
    """@brief Trieda vykonávajúca lexikálnu analýzu.

    @author Jakub Kasem xkasem02
    """
    def __init__(self, expression):
        """@brief Inicializácia triedy.

        Args:
            @param expression (str): Výraz, nad ktorým má byť lexikálna analýza prevedená.
        """
        self.expression: str = expression
        self.pos = 0
        self.currentChar: str = self.expression[self.pos]
        self.tokens = []

    def advance(self):
        """@brief Postup v reťazci o jeden znak.
        """
        self.pos += 1
        if self.pos >= len(self.expression):
            self.currentChar = None
        else:
            self.currentChar = self.expression[self.pos]

    def skipWhitespace(self):
        """@brief Preskočenie bielych znakov.
        """
        while self.currentChar is not None and self.currentChar.isspace():
            self.advance()

    def get_number(self):
        """@brief Extrakcia čísla z výrazu.

        @return str: číslo reprezentované ako reťazec.
        """
        result = ""
        while self.currentChar is not None and self.currentChar.isdigit():
            result += self.currentChar
            self.advance()

        if self.currentChar == ".":
            result += self.currentChar
            self.advance()

            while self.currentChar is not None and self.currentChar.isdigit():
                result += self.currentChar
                self.advance()

        return float(result)

    def get_next_token(self):
        """ @brief Táto metóda vráti ďalší token zo vstupného reťazca výrazov.
        Skontroluje aktuálny znak a vráti zodpovedajúci objekt Token.
        Metóda prechádza reťazec vstupného výrazu a volá ďalšie metódy
        na vynechanie bielych znakov a prípadné získanie čísel.

        Raises:
           @exceptions ValueError: ak je aktuálny znak neplatný a nezodpovedá žiadnemu z definovaných tokenov.

        
        @return Token: Objekt Token predstavujúci ďalší token vo vstupnom reťazci výrazu.
        """
        while self.currentChar is not None:
            if self.currentChar.isspace():
                self.skipWhitespace()
                continue

            if self.currentChar.isdigit() or self.currentChar == ".":
                return Token("NUMBER", self.get_number())

            if self.currentChar == "+":
                self.advance()
                return Token("PLUS", "+")

            if self.currentChar == "-":
                self.advance()
                return Token("MINUS", "-")

            if self.currentChar == "*":
                self.advance()
                return Token("MULTIPLY", "*")

            if self.currentChar == "/":
                self.advance()
                return Token("DIVIDE", "/")

            if self.currentChar == "%":
                self.advance()
                return Token("PERCENT", "%")

            if self.currentChar == "!":
                self.advance()
                return Token("FACTORIAL", "!")

            if self.currentChar == "^":
                self.advance()
                return Token("POWER", "^")
            
            if self.currentChar == "\u221a":
                self.advance()
                return Token("SQRT", "\u221a")

            if self.currentChar == "(":
                self.advance()
                return Token("LBRACKET", "(")

            if self.currentChar == ")":
                self.advance()
                return Token("RBRACKET", ")")

            raise ValueError(f"Invalid character: {self.currentChar}")

        return Token("EOF", None)
 
class Parser:
    """@brief Trieda vykonávajúca lexikálnu a syntaktickú analázu.
    """
    def __init__(self, input):
        """@brief Funkcia inicializuje objekt Parser so vstupným reťazcom.
        Trieda vytvorí objekt Lexer a zavolá jeho metódu get_next_token() na získanie prvého tokenu.
        Objekt Parser sleduje aktuálny token a zoznam všetkých tokenov.

        
         @param   str: Vstupný reťazec, ktorý sa má analyzovať.
        """
        self.lexer = Lexer(input)
        self.current_token = self.lexer.get_next_token()
        self.tokens = [self.current_token]

    def parse(self):
        """@brief Metóda analyzuje vstupný reťazec výrazov volaním metódy expr.

        Raises:
          @exceptions  SyntaxError: Ak po rozbore výrazu zostane nejaký token, zobrazí sa chyba SyntaxError.
        """
        self.expr()
        if self.current_token.token_type != "EOF":
            raise SyntaxError("Invalid syntax")

    def expr(self):
        """@brief Metóda predstavuje výraz vo vstupnom reťazci.
        Najprv zavolá metódu term, aby spracovala ľavú stranu výrazu.
        Potom prechádza vstupný reťazec a kontroluje operátory sčítania alebo odčítania.
        Ak sa nejaký nájde, použije aktuálny token a zavolá metódu term na spracovanie pravej strany výrazu.
        """
        self.term()
        while self.current_token.token_type in ["PLUS", "MINUS"]:
            token = self.current_token
            self.eat(token.token_type)
            if token.token_type == "PLUS":
                self.term()
            else:
                self.term()

    def term(self):
        """@brief Metóda predstavuje výraz vo vstupnom reťazci.
        Najprv zavolá metódu factor na spracovanie ľavej strany výrazu.
        Potom prechádza vstupný reťazec a kontroluje, či sa v ňom nenachádzajú operátory násobenia, delenia, modulu alebo mocniny.
        Ak sa nejaký nájde, použije aktuálny token a zavolá metódu factor na spracovanie pravej strany výrazu.
        """
        self.factor()
        while self.current_token.token_type in ["MULTIPLY", "DIVIDE", "PERCENT", "POWER"]:
            token = self.current_token
            self.eat(token.token_type)
            self.factor()

    def factor(self):
        """ @brief Táto metóda predstavuje výraz vo vstupnom reťazci.
        Najprv získa aktuálny token a skontroluje jeho typ.
        Ak je aktuálnym tokenom otváracia zátvorka, spotrebuje ju, zavolá metódu expr na vyhodnotenie výrazu vnútri zátvorky a potom spotrebuje uzatváraciu zátvorku.
        Ak je aktuálnym tokenom číslo, použije ho.
        Ak je aktuálnym tokenom operátor odmocniny, spotrebuje ho a zavolá metódu expr na vyhodnotenie výrazu vnútri odmocniny.
        Ak je aktuálny token operátor faktoriálu, použije ho a zavolá metódu expr na vyhodnotenie výrazu vnútri faktoriálu.
        Ak je aktuálnym tokenom operátor mocniny, použije ho a zavolá metódu expr na vyhodnotenie výrazu napravo od operátora mocniny.

        Raises:
           @exceptions SyntaxError: ak aktuálny token nie je žiadnym z vyššie uvedených.
        """
        token = self.current_token
        if token.token_type == "LBRACKET":
            self.eat("LBRACKET")
            self.expr()
            self.eat("RBRACKET")
        elif token.token_type == "NUMBER":
            self.eat("NUMBER")
        elif token.token_type == "SQRT":
            self.eat("SQRT")
            self.expr()
        elif token.token_type == "FACTORIAL":
            self.eat("FACTORIAL")
            self.expr()
        elif token.token_type == "POWER":
            self.eat("POWER")
            self.expr()
        elif token.token_type == "PERCENT":
            self.eat("PERCENT")
            self.expr()
        else:
            raise SyntaxError("Invalid syntax")

    def eat(self, token_type):
        """@brief Táto metóda spotrebuje aktuálny token, ak jeho typ zodpovedá zadanému typu tokenu.
        Ak sa typ aktuálneho tokenu zhoduje, metóda aktualizuje aktuálny token zavolaním metódy get_next_token lexera a pripojí nový token do zoznamu tokens.

        Args:
            @param token_type (str): požadovaný typ tokenu.

        Raises:
           @exceptions SyntaxError: ak sa typ aktuálneho tokenu nezhoduje.
        """
        if self.current_token.token_type == token_type:
            self.current_token = self.lexer.get_next_token()
            self.tokens.append(self.current_token)
        else:
            raise SyntaxError("Invalid syntax")

class Controller:
    """Documentation for a class.
 
    More details.
    """

    ## @brief Tento slovník definuje operátory použité vo vstupnom reťazci a ich príslušné úrovne priority.
    ## Operátory sú reprezentované ako kľúče a ich úrovne priority sú reprezentované ako celočíselné hodnoty.
    ## Vyššia hodnota precedensu označuje vyššiu úroveň precedensu.
    ## Poradie operátorov v slovníku určuje poradie, v akom sa vyhodnocujú pri absencii zátvoriek.
    operators = {
            "PLUS": 1,
            "MINUS": 1,
            "MULTIPLY": 2,
            "DIVIDE": 2,
            "FACTORIAL": 3,
            "POWER": 3,
            "SQRT": 3,
            "PERCENT": 3,
        }
    
    def __init__(self):
        """@brief Konštruktor triedy Calculator.
        Inicializuje prázdny zásobník na uloženie operandov a prázdny reťazec na uloženie postfixového výrazu.
        Taktiež inicializuje premennú result na hodnotu None.
        """
        self.stack = []
        self.postfix = ''
        self.result: float or None = None

    def parse(self, expression: str):
        """@brief Táto metóda analyzuje vstupný výraz vytvorením inštancie triedy Parser a zavolaním jej metódy parse.

        Args:
            @param expression (str): vstupný výraz

        Returns:
            Ak je operácia parsovania úspešná, vráti tuple pozostávajúci z logickej hodnoty True označujúcej úspech a zoznamu tokenov získaných z operácie parsovania.
            Ak operácia parsovania vyvolá výnimku, vracia tuple pozostávajúci z logickej hodnoty False označujúcej neúspech a z hodnoty None ako druhej hodnoty.
        """
        try:
            parser = Parser(expression)
            parser.parse()
            return True, parser.tokens
        except Exception as ex:
            return False, None
   
    def calc(self, expression):
        """@brief Táto metóda prijíma ako vstup výraz a vyhodnocu ho:
        1. Vynuluje zásobník a postfixové premenné výrazu.
        2. Zavolá metódu "parse" na získanie zoznamu tokenov zo vstupného reťazca výrazov.
        3. Ak operácia parsovania zlyhá, vráti príkaz 'Syntax ERROR'.
        4. Pomocou metódy 'toPostfix' prevedie zoznam tokenov na postfixový výraz.
        5. Vyhodnotí postfixový výraz pomocou metódy 'evaluate' a získa výsledok.
        6. Ak vyhodnotenie zlyhá, vráti hodnotu 'Math ERROR'.
        7. V opačnom prípade vráti reťazcovú reprezentáciu výsledku.

        Args:
           @param expression (str): vstupný výraz

        Returns:
            @return str: výsledok vyhodnotenia
        """
        self.stack = []
        self.postfix = ''
        valid, tokens = self.parse(expression)
        if not valid:
                return 'Syntax ERROR'
        try:
            self.toPostfix(tokens)
            return str(self.evaluate())
        except Exception as ex:
            return 'Math ERROR'

    def toPostfix(self, tokens):
        """@brief Prevedie infixový matematický výraz na postfixový zápis.

        Args:
            @param tokens (list): Zoznam objektov Token reprezentujúcich infixový matematický výraz.

        Returns:
           @return str: Postfixový zápis výrazu.
        """
        
        for token in tokens:
            if token.token_type == "NUMBER":
                self.postfix += f'{token.value} '
            elif token.token_type == "LBRACKET":
                self.stack.append(token)
            elif token.token_type in self.operators.keys():
                self.handleOperator(token)
            elif token.token_type == "RBRACKET":
                self.handleBracketPair()
            elif token.token_type == "EOF":
                while len(self.stack) > 0:
                    self.postfix += f'{self.stack.pop().value} '
                self.postfix += '='
        
        return self.postfix
    
    def handleOperator(self, token: Token):
        """@brief Metóda handleOperator sa používa na spracovanie operátorových tokenov s cieľom previesť vstupný infixový výraz na postfixový výraz.
        Keď sa vyskytne token operátora, metóda skontroluje, či sa na zásobníku nenachádzajú operátory, ktoré majú vyššiu prioritu ako aktuálny operátor.
        Ak tam žiadny nie je, aktuálny operátor sa presunie na zásobník.
        Ak sa na zásobníku nachádzajú operátory s vyššou prioritou, sú zo zásobníka vybraté a pripojené k postfixovému výrazu, kým sa na ňom nenachádzajú
        ďalšie operátory s vyššou prioritou, a potom je na zásobník presunutý aktuálny operátor.

        Args:
            @param token (Token): operátorový token
        """
        if len(self.stack) == 0 or self.stack[-1].token_type == 'LBRACKET' or self.hasHigherPriority(token):
            self.stack.append(token)
            return
        else:
            if not self.hasHigherPriority(token):
                top = self.stack.pop()
                self.postfix += f'{top.value} '
                self.handleOperator(token)

    def handleBracketPair(self):
        """@brief Táto metóda spracúva dvojicu zátvoriek v infixovom výraze pri prevode na postfixový zápis.
        Vysúva operátory zo zásobníka a pripája ich k postfixovému výrazu, kým sa nenájde a neodstráni príslušná ľavá zátvorka.
        """
        while True:
            token = self.stack.pop()
            if token.token_type == 'LBRACKET':
                break
            self.postfix += f'{token.value} '

    def isNumber(self, token: str):
        """@brief Táto implementácia metódy isNumber() kontroluje, či sa daný reťazcový token dá previesť na číslo typu float.

        Args:
            @param token (str): vstupný token

        Returns:
           @return bool: Ak sa token dá previesť na float, metóda vráti hodnotu True. V opačnom prípade vráti hodnotu False.
        """
        try:
            float(token)
            return True
        except Exception:
            return False
        
    def hasHigherPriority(self, token: Token):
        """@brief Metóda, ktorá preberá objekt Token reprezentujúci operátor a kontroluje, či má vyššiu prioritu ako operátor na vrchole zásobníka.

        Args:
           @param token (Token): vstupný token

        Returns:
            @return bool: pravdivostná hodnota či je priorita vstupného tokena vyššia ako operátor na vrchole zásobníka.
        """
        top = self.stack[-1]

        tokenPrio = self.operators[token.token_type]
        topPrio = self.operators[top.token_type]

        return tokenPrio > topPrio

    def evaluate(self):
        """@brief Metóda evaluate preberá postfixový zápis matematického výrazu a vyhodnocuje ho pomocou dátovej štruktúry zásobníka.

        Returns:
           @return str: vyhodnotenie výrazu.
        """
        self.stack = []
        binary_operands = ['+', '-', '*', '/', '^']
        unar_operands = ['!', '%', '\u221a']

        for znak in self.postfix.split(" "):
            if self.isNumber(znak):
                self.stack.append(znak)
            elif znak == '=':
                return self.stack.pop()
            elif znak in binary_operands:
                self.operand_y = self.stack.pop()
                self.operand_x = self.stack.pop()
                self.result = self.choose_func_to_evaluate_two(self.operand_x, self.operand_y, znak)
                self.stack.append(self.result)
            elif znak in unar_operands:
                self.operand_x = self.stack.pop()
                self.result = self.choose_func_to_evaluate_one(self.operand_x, znak)
                self.stack.append(self.result)
        return self.stack.pop()

    def choose_func_to_evaluate_two(self, operand_x, operand_y, znak):
        """@brief Táto metóda prijíma ako argumenty dva operandy a symbol operátora a na základe symbolu operátora
        vyberie vhodnú matematickú funkciu na ich vyhodnotenie.

        Returns:
            @return Výsledok matematickej operácie.
        """
        if znak == '+':
            return ml.add(float(operand_x), float(operand_y))
        elif znak == '-':
            return ml.sub(float(operand_x), float(operand_y))
        elif znak == '*':
            return ml.mul(float(operand_x), float(operand_y))
        elif znak == '/':
            return ml.div(float(operand_x), float(operand_y))
        elif znak == '^':
            return ml.power(float(operand_x), float(operand_y))
        
    def choose_func_to_evaluate_one(self, operand_x, znak):
        """@briefTáto metóda prijíma ako argumenty jeden operand a symbol operátora a na základe symbolu operátora
        vyberie vhodnú matematickú funkciu na ich vyhodnotenie.

        Returns:
            @return Výsledok matematickej operácie.
        """
        if znak == '!':
            return ml.fac(float(operand_x))
        elif znak == '%':
            return ml.perc(float(operand_x))
        elif znak == '\u221a':
            return ml.root(float(operand_x), 2.0)
        