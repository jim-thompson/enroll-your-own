PYUIC5 = pyuic5-3.7

%.py: %.ui
	$(PYUIC5) $< -o $@
%_rc.py: %.qrc
	$(PYRCC5) $< -o $@

OBJS = \
     ui_mainwindow.py

all: $(OBJS)

clean:
	rm -f $(OBJS)
