import os
import tempfile
import shutil
from click.testing import CliRunner
from src.mlcookiecutter.main import create_project

def test_create_project():
    runner = CliRunner()
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        result = runner.invoke(create_project, ['--project_name', 'test_project', '--license_type', 'mit', '--codeowners', 'test@example.com'])
        assert result.exit_code == 0
        assert os.path.exists('test_project')
        assert os.path.exists('test_project/README.md')
        assert os.path.exists('test_project/LICENSE')
        assert os.path.exists('test_project/CODEOWNERS')

def test_create_project_with_existing_directory():
    runner = CliRunner()
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        os.mkdir('existing_project')
        result = runner.invoke(create_project, ['--project_name', 'existing_project', '--license_type', 'mit', '--codeowners', 'test@example.com'])
        assert result.exit_code == 0
        assert os.path.exists('existing_project/README.md')

def test_invalid_license_type():
    runner = CliRunner()
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        result = runner.invoke(create_project, ['--project_name', 'test_project', '--license_type', 'invalid', '--codeowners', 'test@example.com'])
        assert result.exit_code == 0
        assert "Failed to fetch license" in open('test_project/LICENSE').read()
