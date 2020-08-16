#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 13:27:00 2020

@author: thomasmuat
"""

import betfairlightweight

from variables import username, password, apikey, creds_path

trading = betfairlightweight.APIClient(username,
                                       password,
                                       app_key=apikey,
                                       certs=creds_path)

trading.login()

balance = trading.account.get_account_funds()

print('Your current balance is %s' % balance.available_to_bet_balance)

trading.logout