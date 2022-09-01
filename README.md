# HEAuth

## HEAuth - it's a service for accounting access to critical data for your system.

It is blockchain-based and shows up well in heavily loaded systems

The service runs as a separate container. So it can easily be integrated into kuberneteus.

At the moment the postgress database is used for the needs of the service inside the container.
If you use Postgress on your project you can create a table and redirect the connection to Postgress to your database.
If not, you need to leave the postgress database inside the container.  

>For better analysis we use PgAdmin

Envoy is used to improve fault tolerance.
If you use prometheus + grafana on your project, you can set up a monitoring system and an alert system for envoy.

## Alpha in 2 weeks
