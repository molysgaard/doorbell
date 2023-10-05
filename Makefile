# Define the installation directory for the systemd service file
SYSTEMD_DIR = /etc/systemd/system

# Define the service file name
SERVICE_FILE = doorbell.service

install:
	sudo cp $(SERVICE_FILE) $(SYSTEMD_DIR)
	sudo systemctl daemon-reload
	sudo systemctl enable $(SERVICE_FILE)
	sudo systemctl start $(SERVICE_FILE)

uninstall:
	sudo systemctl stop $(SERVICE_FILE) || true
	sudo systemctl disable $(SERVICE_FILE) || true
	sudo rm -f $(SYSTEMD_DIR)/$(SERVICE_FILE)
	sudo systemctl daemon-reload

.PHONY: install uninstall

