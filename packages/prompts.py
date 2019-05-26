from . import inputs

class MadLibPrompt(object):
    def __init__(self):
        self.be_kind_lib = ""
        self.war_lib = ""

        self.mad_lib_num = 0
        self.mad_lib_name = ""

        self.mad_lib_inputs = []

    def mad_lib_chooser(self):
        print("Choose a mad lib.")
        self.mad_lib_num = input("(1) be kind\n"
                                 "(2) war\n")
        return self.mad_lib_num

    def populate_mad_lib(self):
        self.mad_lib_inputs = inputs.UserInput.populate_input_array(self, int(self.input_amount_dict[self.mad_lib_name]))

    def translate_mad_lib(self):
        self.mad_lib_name = self.mad_lib_translater_dict[int(self.mad_lib_num)]

    def mad_lib_caller(self):
        self.mad_lib_method_dict[int(self.mad_lib_num)](self, self.mad_lib_inputs)

    def be_kind(self, input_array):
        self.be_kind_lib = ("\nBe kind to your {0}-footed {1}\n"
                      "For a duck may be somebody's {2},\n"
                      "Be kind to your {3} in {4}\n"
                      "Where the weather is always {5}.\n"
                      "\nYou may think that this is the {6},\n"
                      "Well it is." .format(input_array[0], input_array[1], input_array[2],
                      input_array[1], input_array[3], input_array[4], input_array[5]))

        print(self.be_kind_lib)
        return self.be_kind_lib

    def war(self, input_array):
        self.war_lib = ("\nIt was during the battle of {0} when I was running through a {1}\n"
                   "when a {2} went off right next to my platoon. Our {3} yelled for\n"
                   "us to {4} to the nearest {5} we could find. When we got to the {6}\n"
                   "we {7} to start a fire. As we were starting the fire the enemy\n"
                   "saw the {8} from the fire and started {9} {10} at us. we all quickly\n"
                   "ducked behind the {11} at the {12} and returned fire. we quickly\n"
                   "eliminated the enemy and were {13} that we had won the battle.\n"
                   .format(input_array[0], input_array[1], input_array[2], input_array[3],
                   input_array[4], input_array[5], input_array[5], input_array[6],
                   input_array[7], input_array[8], input_array[9], input_array[10],
                   input_array[6], input_array[11]))

        print(self.war_lib)
        return self.war_lib

    mad_lib_method_dict = {
        1 : be_kind,
        2 : war
        }

    mad_lib_translater_dict = {
        1 : "be_kind",
        2 : "war"
        }

    input_amount_dict = {
        "be_kind" : 6,
        "war" : 12
    }
