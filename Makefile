PY?=py
#PELICAN?=./pelican/Scripts/pelican.exe
PELICAN?=pelican
PELICANOPTS=
PORT=8001

# BASEDIR=$(CURDIR)
BASEDIR=.

# BASEDIR=M:/Documents/pelican
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py
CUSTOM_DOMAIN_NAME=www.stevehemingway.com
CACHEDIR=$(BASEDIR)/__pycache__


GITHUB_PAGES_BRANCH=master
GITHUB_SOURCE_BRANCH=content


DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif

help:
	@echo 'Makefile for a pelican Web site                                           ';
	@echo '                                                                          ';
	@echo 'Usage:                                                                    ';
	@echo '   make html                           (re)generate the web site          ';
	@echo '   make clean                          remove the generated files         ';
	@echo '   make regenerate                     regenerate files upon modification ';
	@echo '   make publish                        generate using production settings ';
	@echo '   make serve [PORT=8000]              serve site at http://localhost:8000';
	@echo '   make serve-global [SERVER=0.0.0.0]  serve (as root) to $(SERVER):80    ';
	@echo '   make devserver [PORT=8000]          serve and regenerate together      ';
	@echo '   make ssh_upload                     upload the web site via SSH        ';
	@echo '   make rsync_upload                   upload the web site via rsync+ssh  ';
	@echo '   make github                         upload the web site via gh-pages   ';
	@echo '   make upload                         do a git push to github ';
	@echo '   make repo			      commit your recent content changes' ;
	@echo '   make content			      commit your recent content changes' ;
	@echo '   make whole			      combo of repo, upload and github' ;
	@echo '                                                                          ';
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   ';
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    ';
	@echo '                                                                          ';

whole: repo upload github
	date;

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	coreutils [ ! -d $(OUTPUTDIR) ]  || coreutils rm -rf $(OUTPUTDIR)
	coreutils [ ! -d $(CACHEDIR) ]  || coreutils rm -rf $(CACHEDIR)

regenerate:
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

repo:	clean 
	git add $(INPUTDIR)
	git commit -m 'new content' 
	git push

serve:
ifdef PORT
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT)
else
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)
endif

serve-global:
ifdef SERVER
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT) -b $(SERVER)
else
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT) -b 0.0.0.0
endif


devserver:
ifdef PORT
	$(PELICAN) -lr $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT)
else
	$(PELICAN) -lr $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)
endif

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)
# 	echo $(CUSTOM_DOMAIN_NAME) > $(OUTPUTDIR)/CNAME ! I don't think this is needed if we use the -c flag of ghp-import

github: publish 
# first generate the branch
	ghp-import -m "Generate Pelican site" -c $(CUSTOM_DOMAIN_NAME) -f -p -b $(GITHUB_PAGES_BRANCH) $(OUTPUTDIR)
# -c generates a CNAME record
# -p does a push, which makes the following redundant
	git push origin $(GITHUB_PAGES_BRANCH)
	echo "You probably want to git add the content changes too. You've updated only the master branch so far."



.PHONY: html help clean regenerate serve serve-global devserver publish github repo upload 
