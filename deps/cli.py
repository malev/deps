'''In the Shouth you can say: "fix me a sandwich".
Here you'll say: "fix me an environment"
    deps install
    deps install --dry-run
'''

from __future__ import absolute_import
import subprocess
import sys
import yaml


def run(cmd):
    process = subprocess.Popen(cmd, universal_newlines=True)
    process.communicate()


def print_cmd(cmd):
    print(' '.join(cmd))


def build_conda_cmd(specs, channels=[]):
    conda_cmd = ['conda', 'install'] + specs
    if len(channels) > 0:
        channels_cmd = []
        for channel in channels:
            channels_cmd.append('-c')
            channels_cmd.append(channel)
        conda_cmd = conda_cmd + channels_cmd

    return conda_cmd


def build_pip_cmd(specs, **kwargs):
    return ['pip', 'install', ] + specs


def parse():
    try:
        with open('environment.yml', 'r') as envfile:
            parsed = yaml.load(envfile)
    except:
        print("[Error] You will need an environment.yml file")
        sys.exit(1)
    conda_deps = []
    pip_deps = []
    channels = parsed.get('channels', [])
    for dependency in parsed.get('dependencies', []):
        if isinstance(dependency, dict):
            for pip_dep in dependency.get('pip', []):
                pip_deps.append(pip_dep)
        else:
            conda_deps.append(dependency)

    return conda_deps, pip_deps, channels


def not_install():
    conda_deps, pip_deps, channels = parse()
    print("NOT installing:")
    print_cmd(build_conda_cmd(conda_deps, channels=channels))
    print_cmd(build_pip_cmd(pip_deps))
    print("Done.")


def install():
    conda_deps, pip_deps, channels = parse()
    print("Installing:")
    run(build_conda_cmd(conda_deps, channels=channels))
    run(build_pip_cmd(pip_deps))
    print("Done.")


def main():
    if 'install' in sys.argv:
        if '--dry-run' in sys.argv:
            not_install()
        else:
            install()
    elif 'conda' in sys.argv:
        print(" ".join(parse()[0]))
    elif 'pip' in sys.argv:
        print(" ".join(parse()[1]))
    elif 'channels' in sys.argv:
        print(" ".join(parse()[2]))
    else:
        print(__doc__)
