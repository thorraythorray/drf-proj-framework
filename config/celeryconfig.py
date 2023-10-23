# Automatic routing
task_queues = {
    'traffic': {
        'exchange': 'traffic_ex',
    },
}

task_routes = {
    'workers.traffic.*': {
        'queue': 'traffic',
        'routing_key': 'traffic',
    },
}

timezone = 'Asia/Shanghai'