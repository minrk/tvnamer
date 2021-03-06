#!/usr/bin/env python
#encoding:utf-8
#author:dbr/Ben
#project:tvnamer
#repository:http://github.com/dbr/tvnamer
#license:Creative Commons GNU GPL v2
# http://creativecommons.org/licenses/GPL/2.0/

"""Test tvnamer's config loading and saving
"""

import os
import tempfile

from tvnamer.config import Config


def test_saving_loading():
    """Tests saving the default config to a temp folder, and reloading it
    """

    # Save config
    fid, fname = tempfile.mkstemp()
    Config.useDefaultConfig()
    Config.saveConfig(fname)
    assert len(open(fname).read()) > 10, "Config file is less than 10 characters long"

    # Make copy of config dict
    saved_config = dict(Config)

    # Clear config
    Config.loadConfig(fname)
    new_config = dict(Config)

    # Show differences between the two dictionaries, to help debugging errors
    for nk in new_config.keys():
        for sk in saved_config.keys():
            if new_config[nk] != saved_config[nk]:
                print "new_config[%s] (%s) != saved_config[%s] (%s)" % (nk, new_config[nk], nk, saved_config[nk])
            if new_config[sk] != saved_config[sk]:
                print "new_config[%s] (%s) != saved_config[%s] (%s)" % (sk, new_config[sk], sk, saved_config[sk])

    assert saved_config == new_config, "Configs do not match"

    # Clear config
    os.close(fid)

if __name__ == '__main__':
    import nose
    nose.main()
