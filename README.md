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

## Alpha in 2 weeks 15.09.2022

Alpha Version Description
-------------------------

This service allows you to monitor access to critical data, such as personal user data in your applications. The system stores each login and logout in a separate block. All user actions are recorded separately and saved after the user logs out.

Once a user has successfully logged in and created a logon block, a unique token is returned to the user, which is required to confirm his/her identity every time he/she performs an action
>You can customize these actions in your application, for example, opening a database or creating a new entry/editing/deleting.

If the token does not match, the system will send a notification to the administrator or security service, providing the user data, the time of login, the action and the time of that action.

The system works through 2 block tables, one table stores active blocks - i.e. when the user is logged in but not yet logged out and performs any actions in the system *(in the future the system will have an idle-timeout setting)*. The second table stores the closed blocks - that is, it stores the login time for the user, his actions and the exit time.

At any time you have the opportunity to look at both tables and make sure that there are no anomalies!
