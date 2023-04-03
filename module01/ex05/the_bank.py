# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    the_bank.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phijano- <phijano-@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/17 09:59:50 by phijano-          #+#    #+#              #
#    Updated: 2023/03/17 13:39:30 by phijano-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount

class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []
    
    def add(self, new_account):
        """ Add new_account in the Bank
            @new_account: Account() new account to append
            @return   True if success, False if an error occured
        """
        # test if new_account is an Account() instance and if
        # it can be appended to the attribute accounts
        # ... Your code ...

        if not Bank.validator(new_account) or any(new_account.name == x.name for x in self.accounts):
            return False
        else:
            self.accounts.append(new_account)
            return True
    
    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
            @origin:  str(name) of the first account
            @dest:    str(name) of the destination account
            @amount:  float(amount) amount to transfer
            @return   True if success, False if an error occured
        """
        # ... Your code ...

        if not Bank.validator(origin) or not Bank.validator(dest) or amount < 0 or origin.value < amount:
            return False
        else:
            if not origin == dest:
                origin.value -= amount
                dest.value += amount
            return True

    def fix_account(self, name):
        """ fix account associated to name if corrupted
            @name:   str(name) of the account
            @return  True if success, False if an error occured
        """
        # ... Your code ...
        setattr(self, "addr", "asdd")
        return True
  

#        if isinstance(name, str) and any(name == x.name for x in self.accounts):
 #            for x in self.accounts:
  #              if name == x.name:
   #                 account = x
          # for x in dir(self):
            #    if x not in dir(account):
             #       delattr(account, x)
    #        vars_dictionary = vars(account)
     #       for x in vars_dictionary.keys():
      #          setattr(self, x, vars_dictionary.get(x))
       #     return True
        #else:
         #   return False

  #  @staticmethod
    def validator(account):
        if isinstance(account, Account):
            if len(vars(account)) % 2 == 1:
                if not any(x.startswith("b") for x in dir(account)):
                    if any(x.startswith("zip") for x in dir(account)) and any(x.startswith("addr") for x in dir(account)):
                        if (hasattr(account, "name") and hasattr(account, "id") and hasattr(account, "value")):
                            if isinstance(getattr(account, "name"), str):
                                if isinstance(getattr(account, "id"), int):
                                    if isinstance(getattr(account, "value"), int) or isinstance(getattr(account, "value"), float):
                                        print("Validated Account")
                                        return True
        else:
            return False
