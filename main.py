import packages

if '__main__' == __name__:

    user = packages.prompts.MadLibPrompt()
    user.mad_lib_chooser()
    user.translate_mad_lib()
    user.populate_mad_lib()
    user.mad_lib_caller()
