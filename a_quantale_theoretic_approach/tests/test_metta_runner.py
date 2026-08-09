"""
Tests that mcbride_runner.metta has correct import paths.
Includes static validation plus a PeTTa runtime integration test when the
``petta`` executable is installed.
"""
import unittest
import os
import shutil
import subprocess


class TestMettaRunnerImports(unittest.TestCase):
    """
    Validates the mcbride_runner.metta import paths without executing MeTTa.
    The original file had bare import names that would fail at runtime.
    """

    def _get_runner_path(self):
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base, "mcbride_petta", "mcbride_runner.metta")

    def test_runner_file_exists(self):
        path = self._get_runner_path()
        self.assertTrue(os.path.exists(path),
            f"mcbride_runner.metta not found at {path}")

    def test_no_bare_import_names(self):
        """
        Import statements must use full repo-relative paths, not bare names.
        Bare names like 'quantale_types' fail at MeTTa runtime.
        """
        path = self._get_runner_path()
        with open(path) as f:
            content = f.read()

        forbidden_patterns = [
            "!(import! &self quantale_types)",
            "!(import! &self v_predicate)",
            "!(import! &self quantale_colimit_engine)",
        ]
        for pattern in forbidden_patterns:
            self.assertNotIn(
                pattern, content,
                f"Found bare import name in mcbride_runner.metta: '{pattern}'. "
                f"Use full repo-relative path instead."
            )

    def test_correct_full_path_present_without_duplicate_transitive_imports(self):
        """Import the colimit engine once; it supplies the other modules."""
        path = self._get_runner_path()
        with open(path) as f:
            content = f.read()

        refinement_import = (
            "!(import! &self "
            "a_quantale_theoretic_approach/mcbride_petta/"
            "refinement_loop)"
        )
        self.assertIn(refinement_import, content)

        # quantale_colimit_engine imports these transitively. Importing them a
        # second time duplicates PeTTa rewrite rules and can exhaust its stack.
        self.assertNotIn(
            "!(import! &self "
            "a_quantale_theoretic_approach/core_representation/quantale_types)",
            content,
        )
        self.assertNotIn(
            "!(import! &self "
            "a_quantale_theoretic_approach/core_representation/v_predicate)",
            content,
        )

    def test_mcbride_refine_function_defined(self):
        """mcbride-refine must be defined in the runner."""
        path = self._get_runner_path()
        with open(path) as f:
            content = f.read()
        self.assertIn("mcbride-refine", content)

    def test_quantale_blend_and_refine_defined(self):
        """The full pipeline combinator must be defined."""
        path = self._get_runner_path()
        with open(path) as f:
            content = f.read()
        self.assertIn("quantale-blend-and-refine", content)


class TestMettaRunnerRuntime(unittest.TestCase):
    """Execute every public runner operation in the real PeTTa runtime."""

    @unittest.skipUnless(shutil.which("petta"), "PeTTa executable is not installed")
    def test_public_operations_return_expected_results(self):
        tests_dir = os.path.dirname(os.path.abspath(__file__))
        fixture = "mcbride_runner_runtime_test.metta"

        completed = subprocess.run(
            ["petta", fixture],
            cwd=tests_dir,
            capture_output=True,
            text=True,
            timeout=30,
        )

        self.assertEqual(
            completed.returncode,
            0,
            f"PeTTa runner failed:\nSTDOUT:\n{completed.stdout}\n"
            f"STDERR:\n{completed.stderr}",
        )

        output_lines = completed.stdout.splitlines()
        expected_assertions = [
            "(assertEqual true true)",
            "(assertEqual Amphibian Amphibian)",
            "(assertEqual false false)",
        ]
        for assertion in expected_assertions:
            self.assertIn(
                assertion,
                output_lines,
                f"PeTTa did not return the expected runtime assertion: {assertion}",
            )

if __name__ == "__main__":
    unittest.main()
