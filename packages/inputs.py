class UserInput(object):
    mad_lip_inputs = []

    def populate_input_array(self, mad_lip_inp_amt):

        for i in range(mad_lip_inp_amt):
            self.mad_lip_inputs.append(input("Enter input: "))
