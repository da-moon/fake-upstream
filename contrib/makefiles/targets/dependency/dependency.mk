.PHONY:dependency
.SILENT:dependency
dependency:
	- $(call print_running_target)
	- $(call print_running_target,listing targets defined in contrib/makefiles/targets/dependency/dependency.mk ...)
	- $(call print_running_target,$(DEP_TARGETS))
	- $(call print_completed_target)
.PHONY:refresh-deps
.SILENT:refresh-deps
refresh-deps: 
	- $(call print_running_target)
	- @$(MAKE) --no-print-directory -f $(THIS_FILE) $(DEP_TARGETS)
	- $(call print_completed_target)
DEP_TARGETS = poetry.lock setup.py requirements.txt pipfile
.PHONY:$(DEP_TARGETS)
.SILENT:$(DEP_TARGETS)
$(DEP_TARGETS):
	- $(call print_running_target)
	- $(eval command=$(RM) $@)
	- $(eval command=${command} && dephell deps convert --from=pyproject.toml --to $@)
	- @$(MAKE) --no-print-directory -f $(THIS_FILE) shell cmd="${command}"
	- $(call print_completed_target)