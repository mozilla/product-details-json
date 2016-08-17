# product-details-json

A repository of our product data in JSON format: Updated automatically
from [the source][].

The data will be kept updated by our continuous integration server, and can be found
in the `product-details` directory of this repo. To update the data manually, you can
clone this repo, make sure your [docker][] environment is setup and functioning properly,
and run `./docker-update.sh`.

The primary goal of this repo is to be a source of data for www.mozilla.org. We'll
use a webhook from this repo to trigger updates of these data on the site.

[the source]: https://product-details.mozilla.org/1.0/
[docker]: https://www.docker.com/
