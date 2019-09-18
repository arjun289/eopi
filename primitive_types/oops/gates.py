class LogicGate:
    """
    Generic gate implmentation. Models a logic gate.

    Attributes:
    -----------
        label: Every gate has a label.
        output: Every gate has exactly one output.

    Methods:
    --------
        getLabel(): returns label of the gate.
        getOutput(): returns the output of the gate.
    """

    def __init__(self, label):
        self.label = label
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):
    """
    Models a BinaryGate. Abinary gate is one with two inputs.

    Attributes:
    -----------
        pinA: input pin A.
        pinB: input pin B.

    Methods:
    --------
        getPinA(): prompts for input pinA
        getPinB(): prompts for input pinB
    """

    def __init__(self, label):
        # initialize the parent first
        LogicGate.__init__(self, label)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        """
        Checks if pinA is none, if yes, takes user input.
        If the pin is connected to a connector, then asks for the
        ouput of previous gate.
        """
        if self.pinA is None:
            return int(input("Enter Pin A input for gate " +
                       self.getLabel()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        """
        Checks if pinB is none, if yes takes user input.
        If the pin is connected to a connector then asks for the
        ouput of previous gate.
        """
        if self.pinB is None:
            return int(input("Enter Pin B input for gate " +
                       self.getLabel()+"-->"))
        else:
            self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA is None:
            self.pinA = source
        else:
            if self.pinB is None:
                self.pinB = source
            else:
                print("No pins empty on connector")


class UnaryGate(LogicGate):
    """
    Models a unary gate. A unary gate has only one input.

    Attributes:
    ----------
    pin: input pin for the gate.

    Methods:
    --------
    getPin(): prompts to enter pin value.
    """

    def __init__(self, label):
        # initialize the parent first
        LogicGate.__init__(self, label)
        self.pin = None

    def getPin(self):
        if self.pin is None:
            return int(input("Enter Pin input for gate " +
                       self.getLabel()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            print("No pins empty on the Gate")


class AndGate(BinaryGate):
    """
    Models an AND gate.

    Methods:
    -------
    performGateLogic(): performs gate logic as per
                AND gate. 0&0 -> 0, 0&1 -> 0, 1&0 ->0
                1&1 -> 1
    """
    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    """
    Models an OR gate.

    Methods:
    -------
        performGateLogic(): performs gate logic as per
                            OR gate. 0&0 -> 0, 0&1 -> 1, 1&0 -> 1
                            1&1 -> 1
    """
    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 or b == 1:
            return 1
        else:
            return 0


class NotGate(UnaryGate):
    """
    Models a Not gate.
    """
    def __init__(self, label):
        UnaryGate.__init__(self, label)
    
    def performGateLogic(self):
        a = self.getPin()
        if a == 1:
            return 0
        else:
            return 1


class NandGate(AndGate):
    def performGateLogic(self):
        if super.performGateLogic(self) == 1:
            return 0
        else:
            return 1


class NorGate(OrGate):
    def performGateLogic(self):
        if super.performGateLogic(self) == 1:
            return 0
        else:
            return 1


class Connector:
    """
    Models a connector.

    Attributes:
    ----------
        fGate: Gate from which connector starts.
        tgate: Gate at which connector ends.

    Methods:
    --------
        getFrom(): returns from Gate
        getTo(): returns to Gate
    """

    def __init__(self, fgate, tgate):
        self.fgate = fgate
        self.tgate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fgate

    def getTo(self):
        return self.tgate


if __name__ == "__main__":
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g4.getOutput())
