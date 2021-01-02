# Install

Copy service file:
```bash
sudo cp ./home-assistant-sysmon.service /lib/systemd/system/
```

Reload the system manager:
```bash
sudo systemctl daemon-reload
```

Enable the service:
```bash
sudo systemctl enable home-assistant-sysmon.service
```

Start the service
```bash
sudo systemctl start home-assistant-sysmon.service
```

Check status:
```bash
sudo systemctl status home-assistant-sysmon.service
```