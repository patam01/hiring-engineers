initialize(**options)
title = "Amit's Timeboard"
description = "Amit's Timeboard for Panel"
graphs = [{
    "definition": {
        "events": [],
        "requests": [
            {"q": "my_mteric{host:PATAM10}"},
        ],
    "viz": "timeseries"
    },
    "title": "My_Metric"
},
   { "definition": {
        "events": [],
        "requests": [
            {"q": "anomalies(sqlserver.stats.batch_requests{host:PATAM10}, 'basic', '1e-3', direction='above')"},
        ],
    "viz": "timeseries"
    },
    "title": "Anomalies Sql Batch Requests"
},
   { "definition": {
        "events": [],
        "requests": [
            {"q": "my_mteric{host:PATAM10}.rollup(sum,3600)"}
        ],
    "viz": "timeseries"
    },
    "title": "My_Metric Hourly Rollup"
}]

template_variables = [{
    "name": "PATAM10",
    "prefix": "host",
    "default": "host:PATAM10"
}]

read_only = False
api.Timeboard.create(title=title, 
                    description=description, 
                    graphs=graphs, 
                    template_variables=template_variables, 
                    read_only=read_only)