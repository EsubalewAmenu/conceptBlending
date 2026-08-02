"""
Tests that mcbride_runner.metta has correct import paths.
Does not require a live MeTTa runtime — validates the file content statically.
"""
import unittest
import os

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

    def test_correct_full_paths_present(self):
        """The correct full-path imports must be present."""
        path = self._get_runner_path()
        with open(path) as f:
            content = f.read()

        required_patterns = [
            "a_quantale_theoretic_approach/core_representation/quantale_types",
            "a_quantale_theoretic_approach/core_representation/v_predicate",
            "a_quantale_theoretic_approach/structural_reasoning/quantale_colimit_engine",
        ]
        for pattern in required_patterns:
            self.assertIn(
                pattern, content,
                f"Missing correct import path in mcbride_runner.metta: '{pattern}'"
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

if __name__ == "__main__":
    unittest.main()
