class UserInput(object):
    mad_lib_inputs = []

    def populate_input_array(self, mad_lib_int_amt):

        for i in range(mad_lib_int_amt):
            self.mad_lib_inputs.append(input("Enter input: "))
        return self.mad_lib_inputs
