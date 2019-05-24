import packages

if '__main__' == __name__:

    user = packages.inputs.UserInput()
    user.populate_input_array(8)
    packages.prompts.MadLipPrompt.be_kind(user.mad_lip_inputs)
