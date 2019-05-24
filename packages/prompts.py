class MadLipPrompt:
    def __init__(self):
        self.be_kind_lib = ""

    def be_kind(input_array):
        be_kind_lib = ("Be kind to your {0}-footed {1}\n"
                      "For a duck may be somebody's {2},\n"
                      "Be kind to your {3} in {4}\n"
                      "Where the weather is always {5}.\n"
                      "\nYou may think that this is the {6},\n"
                      "Well it is." .format(input_array[0], input_array[1], input_array[2],
                      input_array[3], input_array[4], input_array[5], input_array[6]))

        print(be_kind_lib)
