import unittest
import pathlib
from mopyregtest import cli

this_folder = pathlib.Path(__file__).absolute().parent

class TestCli(unittest.TestCase):
    def test_generate1(self):
        """
        Testing for default arguments in CLI: mopyregtest generate
        """
        cmd_args = ["generate",
                    str(this_folder / "../examples/generate_tests/gen_tests1"),
                    "BlocksLpDist_from_cli_1",
                    "~/.openmodelica/libraries/Modelica 4.0.0+maint.om/",
                    "Modelica.Blocks.Sources.Sine,Modelica.Blocks.Sources.ExpSine,Modelica.Blocks.Sources.Step"]

        cli.parse_args(cmd_args)

        return

    def test_generate2(self):
        """
        Testing for optional arguments in CLI: mopyregtest generate
        """
        cmd_args = ["generate",
                    "--metric=Lp_dist",
                    "--tol=1.2e-5",
                    str(this_folder / "../examples/generate_tests/gen_tests2"),
                    "BlocksLpDist_from_cli_2",
                    "~/.openmodelica/libraries/Modelica 4.0.0+maint.om/",
                    "Modelica.Blocks.Sources.Sine,Modelica.Blocks.Sources.ExpSine,Modelica.Blocks.Sources.Step"]

        cli.parse_args(cmd_args)

        return

    def test_compare1(self):
        """
        Testing for default arguments in CLI: mopyregtest compare
        """
        cmd_args = ["compare",
                    str(this_folder / "../examples/test_user_defined_metrics/references/SineNoisy_res.csv"),
                    str(this_folder / "../examples/test_user_defined_metrics/references/SineNoisy_res.csv")]

        cli.parse_args(cmd_args)

        return

    def test_compare2(self):
        """
        Testing for optional arguments in CLI: mopyregtest compare
        """
        cmd_args = ["compare",
                    "--metric=Lp_dist",
                    "--tol=2.5e-4",
                    "--validated-cols=sine.y,y",
                    "--fill-in-method=interpolate",
                    str(this_folder / "../examples/test_user_defined_metrics/references/SineNoisy_res.csv"),
                    str(this_folder / "../examples/test_user_defined_metrics/references/SineNoisy_res.csv")]

        cli.parse_args(cmd_args)

        return

    def test_compare3(self):
        """
        Testing for correctly raised error in CLI when comparing different results: mopyregtest compare
        """
        cmd_args = ["compare",
                    "--validated-cols=y",
                    "--fill-in-method=interpolate",
                    str(this_folder / "../examples/test_user_defined_metrics/references/SineNoisy_res.csv"),
                    str(this_folder / "../examples/test_user_defined_metrics/references/Sine_res.csv")]

        self.assertRaises(AssertionError, cli.parse_args, cmd_args=cmd_args)

        return

    def test_compare4(self):
        """
        Testing for tol in CLI when comparing different results with sufficiently large tol: mopyregtest compare
        """
        cmd_args = ["compare",
                    "--validated-cols=y",
                    "--tol=0.012",
                    "--fill-in-method=interpolate",
                    str(this_folder / "../examples/test_user_defined_metrics/references/SineNoisy_res.csv"),
                    str(this_folder / "../examples/test_user_defined_metrics/references/Sine_res.csv")]

        cli.parse_args(cmd_args)

        return
