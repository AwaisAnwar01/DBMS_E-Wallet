 # Digital Wallet

## Documentation

## Introduction

The Digital Wallet Solution System is a platform that allows users to store and manage their digital currency and make transactions with ease. This documentation outlines the entities and attributes of the system, as well as the relationships between them.

## Entities

### Currency Supported
```
- Currency ID (primary key represented with underline)
- Currency info id(Foreign key)
- USD equivalent
- Status – (0)active, (1)inactive
```


### Currency Info
```
- Currency info id(Primary key)
- Currency Name 
- Currency Symbol


```
### Deposit
```
- Deposit ID (primary key represented with underline)
- Transaction code
- Member ID (foreign key)
- Deposit amount
- Currency ID
- Date time
- Payment gateway ID
- Status id(foreign key)
```

### Deposit Status
```
- Status id(primary key represented with underline)
- Status
- Remarks
 '''


### Gateway

```
- Gateway ID (primary key represented with underline)
- Gateway name – coins.ph, gcash, paymaya, paypal
- Type – automatic, manual
- Status – (0)active, (1)inactive
```


### User

```

- User ID (primary key represented with underline)
- Usernamea
- Password
- Complete name
- Email address

```

### Member

```

- Member ID (primary key represented with underline)
- First name
- Middle name
- Last name
- Email address
- Country
- Contact number
- Username
- Password
- Account status – (0)pending, (1)approved, (2)cancelled
- Processed by – foreign key

```


### Withdrawal

```
- Withdrawal ID (primary key represented with underline)
- Transaction code
- Member ID (foreign key for user verification)
- Amount
- Charged
- To receive
- Date time
- Method – bank transfer, paypal, etc.
- Status – (0)pending, (1)successful, (2)rejected
- Remarks

```

### Transaction Log

```

- Transaction Log ID (primary key represented with underline)
- Member ID (foreign key)
- Type – (0)deposit, (1)withdrawal
- Amount
- Status – (0)pending, (1)successful, (2)rejected

```

## Relationships

```

- User verifies the registration process of the member (1 to many relationship).
- Member can deposit their money on the platform. Their record appears in the deposit table multiple times (1 to many relationship).
- Currency type is also included in the deposit record or table (1 to many relationship).
- Gateway information is also recorded in the deposit record or table (1 to many relationship).
- Member can request for withdrawal process and the record is being stored in the withdrawal table (1 to many relationship).
- Transaction table or record keeps the information of the members (1 to many relationship).

```

## Conclusion

```

This documentation provides an overview of the entities and relationships within the Digital Wallet Solution System. By understanding these entities and their attributes, users can effectively manage their digital currency and make transactions with ease.


```

## Summary
```

The Digital Wallet Solution System is a platform that enables users to store and manage their digital currency and perform transactions with ease. The system comprises six entities, including Currency Supported, Deposit, Gateway, User, Member, Withdrawal, and Transaction Log. The relationships between these entities have also been defined. The documentation provides an overview of each entity and its attributes, allowing users to effectively manage their digital currency.

```



+--------------+          +------------------+           +----------+
| Currency     |          | Deposit          |           | Gateway  |
+--------------+          +------------------+           +----------+
| Currency_ID  |          | Deposit_ID       |           | Gateway_ID |
| Currency_name|   +----> | Transaction_code |    +---->  | Gateway_name|
| Currency_sym |   |      | Member_ID (FK)   |    |      | Type     |
| USD_equivalent|   |      | Deposit_amount  |    |      | Status   |
| Status       |   |      | Currency_ID (FK) |    |      +----------+
+--------------+   |      | Date_time       |    |
                    |      | Payment_gateway_ID (FK)| 
                    |      | Status          |    |
                    |      | Remarks         |    |
                    |      +------------------+    |
                    |                                |
                    |                                |
+--------------+    |                                |
| User         |    |                                |
+--------------+    |     +---------------------+  |
| User_ID      |    |     | Withdrawal          |  |
| Username     |    |     +---------------------+  |
| Password     |    |     | Withdrawal_ID       |  |
| Complete_name|    |     | Transaction_code    |  |
| Email address|    +---> | Member_ID (FK)      |  |
+--------------+    |     | Amount              |  |
                    |     | Charged             |  |
                    |     | To_receive         |  |
+--------------+    |     | Date_time          |  |
| Member       |    |     | Method              |  |
+--------------+    |     | Status              |  |
| Member_ID    |    |     | Remarks             |  |
| First_name   |    |     +---------------------+  |
| Middle_name  |    |
| Last_name    |    |
| Email_address|    |
| Country      |    |
| Contact_number|   |
| Username     |   |
| Password     |   |
| Account_status|   |
| Processed_by  |   |
+--------------+   |
                    |
+--------------+    |
| Transaction   |    |
+--------------+    |
| Transaction_ID|    |
| Member_ID (FK)|    |
| Type          |    |
| Amount        |    |
| Status        |    |
+--------------+    |
