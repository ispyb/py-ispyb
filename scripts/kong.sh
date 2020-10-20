KONG_DIR=/home/mxuser/software/kong
CONFIG_FILE=$KONG_DIR/conf/kong.conf

HOST=http://localhost
ISPYB_CORE_URL=http://127.0.0.1:5000/ispyb/api/v1
ISPYB_SSX_URL=http://127.0.0.1:5010/ispyb/api/v1/ssx

case "$1" in
 start)
 	echo "Starting kong..."
	sudo kong start -c $CONFIG_FILE
 ;;
 stop)
	echo "Stopping kong..."
	sudo kong stop -p $KONG_DIR
 ;;
  status)
	 echo "Kong status..."
	 sudo kong health -p $KONG_DIR
 ;;
 restart)
	echo "Restarting kong..."
	sudo kong restart -c $CONFIG_FILE
 ;;
 reset)
	echo "Reseting kong..."
	sudo kong migrations reset -c $CONFIG_FILE --v
	sudo kong migrations bootstrap -c $CONFIG_FILE
 ;;
 init)
	echo "Initializing kong services..."
	curl -i -X POST --url $HOST:8001/services/ --data 'name=ispyb_core' --data 'url=http://127.0.0.1:5000/ispyb/api/v1'
	curl -i -X POST --url $HOST:8001/services/ispyb_core/routes --data 'hosts[]=ispyb_core'


	curl -i -X POST --url $HOST:8001/services/ --data 'name=ispyb_ssx' --data 'url=http://127.0.0.1:5010/ispyb/api/v1/ssx'
	curl -i -X POST --url $HOST:8001/services/ispyb_ssx/routes --data 'hosts[]=ispyb_ssx'
 ;;
 test)
 	curl -i -X GET --url $HOST:8000/proposals --header 'Host: ispyb_core' --header  "Authorization: Bearer MasterToken"
	curl -i -X GET --url $HOST:8000/samples --header 'Host: ispyb_ssx' --header  "Authorization: Bearer MasterToken"
 ;;

 *)
 echo "Usage: $0 {start | stop | status | restart | reset | init | test}"
 exit 2
 ;;
esac

exit 0
