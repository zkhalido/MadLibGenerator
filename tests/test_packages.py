from packages import inputs
from packages import prompts
import unittest
from unittest.mock import patch

class InputsTest(unittest.TestCase):
    def setUp(self):
        self.inputs = inputs.UserInput()

    def test_populate_input_array_correct(self):
        return_input_array = []
        mad_lib_int_amt = 6
        user_input = ['Hello', 'my', 'name', 'is', 'Jeff', 'foo']
        expected_array = ['Hello', 'my', 'name', 'is', 'Jeff', 'foo']

        with patch('builtins.input', side_effect=user_input):
            return_array = self.inputs.populate_input_array(mad_lib_int_amt)
        self.assertEqual(return_array, expected_array)

    def test_populate_input_array_incorrect(self):
        return_input_array = []
        mad_lib_int_amt = 6
        user_input = ['Hello', 'my', 'name', 'is', 'Jeff', 'foo']
        expected_array = ['Hello']

        with patch('builtins.input', side_effect=user_input):
            return_array = self.inputs.populate_input_array(mad_lib_int_amt)
        self.assertNotEqual(return_array, expected_array)

class PromptsTest(unittest.TestCase):
    def setUp(self):
        self.prompts = prompts.MadLibPrompt()

    def test_mad_lib_chooser_correct(self):
        user_input = [1]
        expected_return = [1]
        return_value = []

        with patch('builtins.input', side_effect=user_input):
            return_value.append(self.prompts.mad_lib_chooser())
        self.assertEqual(return_value, expected_return)

    def test_mad_lib_chooser_incorrect(self):
        user_input = [1]
        expected_return = [0]
        return_value = []

        with patch('builtins.input', side_effect=user_input):
            return_value.append(self.prompts.mad_lib_chooser())
        self.assertNotEqual(return_value, expected_return)

    def test_be_kind_correct(self):
        input_array = ['', '', '', '', '', '', '']

        expected_output_string = ("\nBe kind to your -footed \n"
                      "For a duck may be somebody's ,\n"
                      "Be kind to your  in \n"
                      "Where the weather is always .\n"
                      "\nYou may think that this is the ,\n"
                      "Well it is.")

        return_value = self.prompts.be_kind(input_array)
        self.assertEqual(return_value, expected_output_string)

    def test_be_kind_incorrect(self):
        input_array = ['0', '1', '2', '3', '4', '5', '6']

        expected_output_string = ("\nBe kind to your -footed \n"
                      "For a duck may be somebody's ,\n"
                      "Be kind to your  in \n"
                      "Where the weather is always .\n"
                      "\nYou may think that this is the ,\n"
                      "Well it is.")

        return_value = self.prompts.be_kind(input_array)
        self.assertNotEqual(return_value, expected_output_string)

    def test_war_correct(self):
        input_array = ['', '', '', '', '', '', '', '', '', '', '', '']

        expected_output_string = ("\nIt was during the battle of  when I was running through a \n"
                   "when a  went off right next to my platoon. Our  yelled for\n"
                   "us to  to the nearest  we could find. When we got to the \n"
                   "we  to start a fire. As we were starting the fire the enemy\n"
                   "saw the  from the fire and started   at us. we all quickly\n"
                   "ducked behind the  at the  and returned fire. we quickly\n"
                   "eliminated the enemy and were  that we had won the battle.\n")

        return_value = self.prompts.war(input_array)
        self.assertEqual(return_value, expected_output_string)

    def test_war_incorrect(self):
        input_array = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']

        expected_output_string = ("\nIt was during the battle of  when I was running through a \n"
                   "when a  went off right next to my platoon. Our  yelled for\n"
                   "us to  to the nearest  we could find. When we got to the \n"
                   "we  to start a fire. As we were starting the fire the enemy\n"
                   "saw the  from the fire and started   at us. we all quickly\n"
                   "ducked behind the  at the  and returned fire. we quickly\n"
                   "eliminated the enemy and were  that we had won the battle.\n")

        return_value = self.prompts.war(input_array)
        self.assertNotEqual(return_value, expected_output_string)
