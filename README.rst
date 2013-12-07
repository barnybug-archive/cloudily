Cloudily - automatically visualize your EC2 infrastructure
==========================================================

.. image:: http://loads.pickle.me.uk/static/images/cloudily.png

Getting Started
---------------

You'll need `graphviz <http://www.graphviz.org/>`_ installed, and optionally
`imagemagick <http://www.imagemagick.org/>`_ to use the ``--preview`` functionality.

On Ubuntu::

    $ sudo apt-get install graphviz imagemagick

Install cloudily from `PyPI <http://pypi.python.org/pypi/graphops>`_ like so::

    $ sudo pip install cloudily

Run cloudily::

    $ cloudily --ec2 instances,elb --conns --preview

Open montage.png in your favourite image viewer::

    $ qiv montage.png

The ``--preview`` makes a montage of the various graphviz layouts available.
Depending on your network usually 'dot' produces the cleaner layouts, but others
may work better / look cooler.

Visualizing EC2 hosts
---------------------
Use the ``--ec2`` option to visualize your EC2 instances and ELBs. Run::

    $ cloudily --ec2 instances,elb --conns --png myarch.png

You need to set your Amazon credentials as environment variables: AWS_ACCESS_KEY_ID
and AWS_SECRET_ACCESS_KEY or configure them in ~/.boto. For more information see:
http://code.google.com/p/boto/wiki/BotoConfig

``--ec2groups`` may be used to filter by security group. This accepts a comma-
separated list of multiple groups. eg. ``--ec2groups group1,group2``

Discovery
---------
There are various ways Cloudily can discover the connections between your
hosts.

``--arp``: Looks at the IP addresses in the arp cache. This has limited use inside
EC2, since hosts are usually on different subnets, but maybe useful for other
setups.

``--conns``: Looks at the currently open UDP and TCP connections for each host. If
the system is active or there is connection pooling (eg. most database
libraries) you should see everything, otherwise there's a chance you'll
not see connections through inactivity.

``--logins``: Includes logins by username in the diagram so you can see who logs
in to which hosts.

Other options
-------------
With ``--conns`` you can also limit to a selection of ports using ``--connsports
80,3306``. This is handy if you're only interested in specific services.

Changelog
---------
0.1.3

- .ssh/config optional

0.1.2

- Fix defaults

0.1.1

- First release
