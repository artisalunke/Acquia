.. include:: /common/global.rst

About websockets
================

A *websocket* is a persistent communication channel open between a
server (based on Node.js) and a client (using a web browser). Messages
can be sent bidirectionally using this method, making websockets useful
for notifications, chat clients, and other content updates that should
appear asynchronously from a traditional page load.

.. _php:

Differences between Node.js and PHP
-----------------------------------

With PHP, each new Drupal request starts a new PHP process, which must
be terminated when the request is completed. For a websocket to function
in a PHP application, the PHP process must always remain open and
waiting for connections instead of terminating. Unfortunately, because
|acquia-product:ac| has a time limit for PHP connections this approach
is not possible.

As a comparison, due to how Node.js is designed implementing a websocket
is trivial, and has valid use cases with a decoupled Drupal
installation. For example, if the websocket server detects a change in
the content managed by Drupal, it pushes those content updates to all
connected clients. Because of this, |acquia-product:ac| supports
implementing a websocket server using Node.js.

.. note::

    Acquia strongly recommends that you test your websocket-based
    applications before deployment. Concurrent websocket connection numbers
    may vary based on server size and application.

.. _use:

Websocket use cases
-------------------

One websocket use case example is having an application that needs
real-time updates (such as a sports scoreboard or a live text feed on a
news website). When the websocket server detects a content change in
Drupal, it pushes updates of your Drupal-managed content to all
connected clients.

Although you could develop this application only using Drupal, doing so
would require each client to poll your web server on a timed basis,
drastically increasing your website's traffic. As an example, if 100,000
visitors were viewing live updates of a game on your website, and each
visitor's browser polled your website for traffic every 10 seconds,
Drupal would receive approximately 600,000 requests per minute. The only
way a traditional Drupal website could handle that much traffic is by
using caching, but this approach would require you to clear the cache
every time a score changed during the game.

By developing this application using a Node.js websocket server, those
same 100,000 clients would each open a websocket, and from that time
forward, only Node.js would determine when to make a Drupal request. If
Node.js contacted Drupal every 10 seconds for updates, those six
requests per minute would then be pushed to all 100,000 website
visitors. Because traffic to the server would be low those six requests
could remain uncached, which would allow Drupal to perform normally.

.. _configure:

Configuring websockets
----------------------

Websockets require a specific path (such as ``/_socket``) on the
|acquia-product:ac| platform.

Websockets also require a path, which can be used by exposing a port for
your application. Acquia exposes a port through the ``process.env.PORT``
variable.

Use of this port for websockets depends on the Node.js library that the
application is using. For specific information about many common
websocket libraries for Node.js, see `Which websocket library to use
with Node.js? <https://stackoverflow.com/questions/16392260/which-websocket-library-to-use-with-node-js/16393046#16393046>`__
on Stack Overflow.

.. _socketio:

Using socket.io
~~~~~~~~~~~~~~~

To use `socket.io <https://socket.io/>`__ in an application hosted on
|acquia-product:ac|, complete the following steps:

#. Set the listening port using ``process.env.PORT``.
#. Set the socket path to ``'/_socket'``.
#. Set the transport for the socket to ``"['websocket']"``.
#. Add the following required parameters to your application:

   .. code-block:: none

      Server:  
      var server = require('http').createServer(app); 
      var io = require('socket.io')(server, { path: '/_socket' }); 
      var port = process.env.PORT || 3000;  
      
      io.set('transports', ['websocket']);  
      
      Client:  var socket = io('example.com', { path: '/_socket', transports: ['websocket'] });``
