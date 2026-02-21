from src.main import main


def test_main_runs(capsys):
    main()
    assert "initialized" in capsys.readouterr().out
