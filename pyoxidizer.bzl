
def make_dist():
    return default_python_distribution()

def make_exe(dist):
    python_config = PythonInterpreterConfig(
        # filesystem_importer=True,
        run_eval="import upstream_gen.__main__; __main__.main()"
    )

    exe = dist.to_python_executable(
        name="upstream-gen",
        config=python_config,
        resources_policy="prefer-in-memory-fallback-filesystem-relative:lib",
        extension_module_filter='all',
        include_sources=False,
        include_resources=False,
        include_test=False
    )
    # exe.add_in_memory_python_resources(dist.pip_install(["-r", "requirements.txt"]))
    # exe.add_in_memory_python_resources(dist.setup_py_install(
    #     package_path=CWD
    # ))
    exe.add_in_memory_python_resources(dist.read_virtualenv("/home/gitpod/.cache/pypoetry/virtualenvs/upstream-gen*"))
    return exe

def make_embedded_resources(exe):
    return exe.to_embedded_resources()

def make_install(exe):
    # Create an object that represents our installed application file layout.
    files = FileManifest()
    # Add the generated executable to our install layout in the root directory.
    files.add_python_resource(".", exe)
    return files

# Tell PyOxidizer about the build targets defined above.
register_target("dist", make_dist)
register_target("exe", make_exe, depends=["dist"], default=True)
register_target("resources", make_embedded_resources, depends=["exe"], default_build_script=True)
register_target("install", make_install, depends=["exe"])

resolve_targets()

# END OF COMMON USER-ADJUSTED SETTINGS.
PYOXIDIZER_VERSION = "0.7.0"
PYOXIDIZER_COMMIT = "UNKNOWN"
