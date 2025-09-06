import os, pytest
def test_artifacts_exist_or_skip():
    missing = [p for p in ["CVaR_Adjusted_Update_Module.pdf","Tests.zip"] if not os.path.exists(p)]
    if missing: pytest.skip("Missing: "+", ".join(missing))
