.PHONY:dependency
.SILENT:dependency
dependency:
	- $(call print_running_target)
	- $(call print_running_target,listing targets defined in contrib/makefiles/targets/dependency/dependency.mk ...)
	- $(call print_running_target,++ make poetry.lock)
	- $(call print_running_target,++ make requirements.txt)
	- $(call print_running_target,++ make setup.py)
	- $(call print_running_target,++ make pipfile)
	- $(call print_running_target,++ make -j$$(nproc) refresh-deps)
	- $(call print_completed_target)
.PHONY:refresh-deps
.SILENT:refresh-deps
refresh-deps: 
	- $(call print_running_target)
	- @$(MAKE) --no-print-directory -f $(THIS_FILE) poetry.lock setup.py requirements.txt pipfile
	- $(call print_completed_target)
.PHONY:poetry.lock
.SILENT:poetry.lock
poetry.lock:
	- $(call print_running_target)
	- $(RM) poetry.lock
	- dephell deps convert --from=pyproject.toml --to poetry.lock
	- $(call print_completed_target)
.PHONY:setup.py
.SILENT:setup.py
setup.py:
	- $(call print_running_target)
	- $(RM) setup.py
	- dephell deps convert --from=pyproject.toml --to poetry.lock
	- $(call print_completed_target)
.PHONY:requirements.txt
.SILENT:requirements.txt
requirements.txt:
	- $(call print_running_target)
	- $(RM) requirements.txt
	- dephell deps convert --from=pyproject.toml --to requirements.txt
	- $(call print_completed_target)

.PHONY:pipfile
.SILENT:pipfile
pipfile:
	- $(call print_running_target)
	- $(RM) Pipfile
	- dephell deps convert --from=pyproject.toml --to Pipfile
	- $(call print_completed_target)
