pkill -f "runserver 0.0.0.0:8000"
if [[ -f /opt/concentrator/web.pid ]]; then
	rm /opt/concentrator/web.pid
fi
