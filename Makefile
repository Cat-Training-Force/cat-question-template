SCRIPT_PREFIX=./scripts

all:
	bash $(SCRIPT_PREFIX)/build.sh && bash $(SCRIPT_PREFIX)/run.sh

run:
	bash $(SCRIPT_PREFIX)/run.sh

build:
	bash $(SCRIPT_PREFIX)/build.sh

stop:
	bash $(SCRIPT_PREFIX)/stop.sh

clean:
	bash $(SCRIPT_PREFIX)/stop.sh ; bash $(SCRIPT_PREFIX)/delete.sh

rebuild:
	bash $(SCRIPT_PREFIX)/stop.sh ; bash $(SCRIPT_PREFIX)/delete.sh ; bash $(SCRIPT_PREFIX)/build.sh ; bash $(SCRIPT_PREFIX)/run.sh

push:
	bash $(SCRIPT_PREFIX)/push.sh

publish:
	bash $(SCRIPT_PREFIX)/build.sh && bash $(SCRIPT_PREFIX)/push.sh