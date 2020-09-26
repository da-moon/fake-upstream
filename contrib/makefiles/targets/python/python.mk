
THIS_FILE := $(lastword $(MAKEFILE_LIST))
SELF_DIR := $(dir $(THIS_FILE))
POETRY := PIP_USER=false python3 $(HOME)/.poetry/bin/poetry
.PHONY:  python-init
.SILENT: python-init
python-init:
	- $(call print_running_target)
	- $(eval command=${POETRY} run python3 -m pip install --upgrade pip)
	- $(eval command=${command} && ${POETRY} update)
	- @$(MAKE) --no-print-directory -f $(THIS_FILE) shell cmd="${command}"
	- @$(MAKE) --no-print-directory -f $(THIS_FILE) python-clean
	- $(call print_completed_target)
.PHONY:  python-server
.SILENT: python-server
python-kill-server:
	- $(call print_running_target)
	- $(eval command=fuser -n tcp -k ${UPSTREAM_PORT})
	- @$(MAKE) --no-print-directory -f $(THIS_FILE) shell cmd="${command}"
	- $(call print_completed_target)
	
.PHONY:  python-server
.SILENT: python-server
python-server: python-kill-server
	- $(call print_running_target)
	- $(eval command=$(MKDIR) logs )
	- $(eval command=${command} && ${POETRY} run cli)
ifneq (${LOG_LEVEL}, )
	- $(eval command=${command} --log ${LOG_LEVEL})
endif
	- $(eval command=${command} server)
ifneq (${UPSTREAM_PORT}, )
	- $(eval command=${command} --port ${UPSTREAM_PORT})
endif
	- $(eval command=${command} > $(PWD)/logs/upstream-server.log 2>&1 &)
	- @$(MAKE) --no-print-directory -f $(THIS_FILE) shell cmd="${command}"
	- @$(MAKE) --no-print-directory -f $(THIS_FILE) python-clean
	- $(call print_completed_target)
.PHONY:  python-clean
.SILENT: python-clean
python-clean:
	- $(call print_running_target)
	- $(eval command=find $(PWD) -type d -name '__pycache__' | xargs -I {} rm -rf {})
	- @$(MAKE) --no-print-directory -f $(THIS_FILE) shell cmd="${command}"

	- $(call print_completed_target)

.PHONY:  python-clean-1
.SILENT: python-clean-1
python-clean-1:
	- $(call print_running_target)
	- $(call print_running_target, removing egg-info directories)
	- $(RM) $(PWD)/*.egg-info
	- $(call print_running_target, removing __pycache__ directories)
	- $(RM) $(call rwildcard,$(PWD)/__pycache__)
	- $(RM) $(call rwildcard,$(PWD)/cmd/__pycache__)
	- $(RM) $(call rwildcard,$(PWD)/cmd/*/__pycache__)
	- $(RM) $(call rwildcard,$(PWD)/cmd/*/*/__pycache__)
	- $(RM) $(call rwildcard,$(PWD)/cmd/*/*/*/__pycache__)
	- $(RM) $(call rwildcard,$(PWD)/cmd/*/*/*/*/__pycache__)
	- $(call print_running_target, removing '*.py.*' files)
	- $(RM) $(call rwildcard,$(PWD)/*.py.*)
	- $(RM) $(call rwildcard,$(PWD)/cmd/*.py.*)
	- $(RM) $(call rwildcard,$(PWD)/cmd/*/*.py.*)
	- $(RM) $(call rwildcard,$(PWD)/cmd/*/*/*.py.*)
	- $(RM) $(call rwildcard,$(PWD)/cmd/*/*/*.py.*)
	- $(RM) $(call rwildcard,$(PWD)/cmd/*/*/*/*.py.*)
	- $(RM) $(call rwildcard,$(PWD)/cmd/*/*/*/*/*.py.*)
	- $(call print_completed_target)
.PHONY:  python
.SILENT: python
python:
	- $(call print_running_target)
	- $(call print_running_target,listing targets defined in contrib/makefiles/targets/python/python.mk ...)
	- $(call print_running_target,++ make python-init)
	- $(call print_running_target,++ make python-server)
	- $(call print_running_target,++ make python-kill-server)
	- $(call print_running_target,++ make python-clean)
ifneq ($(DELAY),)
	- sleep $(DELAY)
endif
	- $(call print_completed_target)



