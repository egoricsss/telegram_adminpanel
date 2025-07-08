import subprocess

from core import config

__all__ = ["run_wireguard_cmd"]


def run_wireguard_cmd(args: list[str]) -> str:
    try:
        result = subprocess.run(
            ["sudo", "bash", config.SCRIPT_PATH] + args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
            timeout=30,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Ошибка:\n{e.stderr.strip()}"
