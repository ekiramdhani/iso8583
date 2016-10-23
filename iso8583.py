#!/usr/bin/env python
#!vim: ts=4:sw=4:tw=80:nowrap

from gi.repository import Gtk

fields = 0x00000000
bits = [
	0x80, 	# = 1000 0000
	0x40, 	# = 0100 0000
	0x20, 	# = 0010 0000
	0x10, 	# = 0001 0000
	0x08, 	# = 0000 1000
	0x04, 	# = 0000 0100
	0x02, 	# = 0000 0010
	0x01	# = 0000 0001
]

builder = Gtk.Builder()
bitmap = [
	[ "1",		"",				"B", 			 "1",		"Bitmap Extended"								],
	[ "2",		"LLVAR",		"N", 		  "..20",		"Primary Account Number (PAN)"					],
	[ "3",		"",				"N", 			 "6",		"Processing Code"								],
	[ "4",		"",				"N", 			"12",		"Amount, Transaction"							],
	[ "5",		"",				"N", 			"12",		"Amount, Settlement"							],
	[ "6",		"",				"N", 			"12",		"Amount, Card holder billing"					],
	[ "7",		"MMDDhhmmss",   "N", 			"10",		"Transmission Date & Time"					],
	[ "8",		"",				"N", 			 "8",		"Amount, Card holder billing fee"				],
	[ "9",		"",				"N", 			 "8",		"Conversion Rate, Settlement"					],
	[ "10",		"",				"N", 			 "8",		"Conversion Rate, Card holder billing"			],
	[ "11",		"",				"N", 			 "6",		"System Trace Audit Number (STAN)"				],
	[ "12",		"hhmmss",		"N", 			 "6",		"Time, Local transaction"						],
	[ "13",		"MMDD",			"N", 			 "4",		"Date, Local transaction"						],
	[ "14",		"YYMM",			"N", 			 "4",		"Date, Expiration"								],
	[ "15",		"MMDD",			"N", 			 "4",		"Date, Settlement"								],
	[ "16",		"MMDD",			"N", 			 "4",		"Date, Conversion"								],
	[ "17",		"MMDD",			"N", 			 "4",		"Date, Capture"									],
	[ "18",		"",				"N", 			 "4",		"Merchant type"									],
	[ "19",		"",				"N", 			 "3",		"Acquiring Institution Country Code"			],
	[ "20",		"",				"N", 			 "3",		"PAN Extended, Country code"					],
	[ "21",		"",				"N", 			 "3",		"Forwarding Institution, Country code"			],
	[ "22",		"",				"N", 			 "3",		"Point Of Service Code"							],
	[ "23",		"",				"N", 			 "3",		"Card Sequence Number"							],
	[ "24",		"",				"N", 			 "3",		"Network International Identifier (NII)"		],
	[ "25",		"",				"N", 			 "2",		"Point Of Service Condition Code"				],
	[ "26",		"",				"N", 			 "2",		"PIN Length Capture"							],
	[ "27",		"",				"N", 			 "1",		"Authorization Identification Response Length"	],
	[ "28",		"",				"N", 			 "8",		"Amount Transaction Fee"						],
	[ "29",		"",				"N", 			 "8",		"Amount Settlement Fee"							],
	[ "30",		"",				"N", 			 "8",		"Amount Transaction Processing Fee"				],
	[ "31",		"",				"N", 			 "8",		"Amount Settlement Processing Fee"				],
	[ "32",		"LLVAR",		"N", 		  "..11",		"Acquiring Institution Identification Code"		],
	[ "33",		"LLVAR",		"N", 		  "..11",		"Forwarding Institution Identification Code"	],
	[ "34",		"LLVAR",		"N", 		  "..28",		"Primary Account Number (PAN) Extended"			],
	[ "35",		"LLVAR",		"Z", 		  "..37",		"Track 2"										],
	[ "36",		"LLLVAR",		"N",		"...104",		"Track 3"										],
	[ "37",		"",			   "AN",			"12",		"Retrieval Reference Number"					],
	[ "38",		"",			   "AN",			 "6",		"Authorization Identification Response"			],
	[ "39",		"",			   "AN",			 "2",		"Response Code"									],
	[ "40",		"",			   "AN", 			 "3",		"Service Restriction Code"						],
	[ "41",		"",			  "ANS",			 "8",		"Card Acceptor Terminal Identification"			],
	[ "42",		"",			  "ANS",			"15",		"Card Acceptor Identification Code"				],
	[ "43",		"",			  "ANS",			"40",		"Card Acceptor Name/Location"					],
	[ "44",		"LLVAR",	  "ANS",		  "..25",		"Additional Response Data"						],
	[ "45",		"LLVAR",	   "AN",		  "..76",		"Track 1 Data"									],
	[ "46",		"LLLVAR",      "AN",		"...999",		"Additional Data ISO"							],
	[ "47",		"LLLVAR",      "AN",		"...999",		"Additional Data National"						],
	[ "48",		"LLLVAR",      "AN",		"...999",		"Additional Data Private"						],
	[ "49",		"",			   "AN",			 "3",		"Currency Code Transaction"						],
	[ "50",		"",			   "AN", 			 "3",		"Currency Code Settlement"						],
	[ "51",		"",			   "AN",		   "255",		"Currency Code Card Holder Billing"				],
	[ "52",		"",				"B", 			"64",		"Person Identification Number (PIN) Data"		],
	[ "53",		"",				"N",			"18",		"Security Related Control Information"			],
	[ "54",		"LLLVAR",      "AN",		"...120",		"Additional Amount"								],
	[ "55",		"LLLVAR",     "ANS",		"...999",		"Reserved ISO"									],
	[ "56",		"LLLVAR",     "ANS",		"...999",		"Reserved ISO"									],
	[ "57",		"LLLVAR",     "ANS",		"...999",		"Amount Cash (AUS Only)"						],
	[ "58",		"LLLVAR",     "ANS",		"...999",		"Ledger Balance (AUS Only)"						],
	[ "59",		"LLLVAR",     "ANS",		"...999",		"Account Balance Cleared Funds (AUS Only)"		],
	[ "60",		"",			  "AN",				 "7",		"Advice/reason code (private reserved)"			],
	[ "61",		"LLLVAR",     "ANS",		"...999",		"Reserved Private"								],
	[ "62",		"LLLVAR",     "ANS",		"...999",		"Reserved Private"								],
	[ "63",		"LLLVAR",     "ANS",		"...999",		"Reserved Private"								],
	[ "64",		"",				"B",			"64",		"Message Authentication Code (MAC)"				],
	[ "65",		"",				"B",			"16",		"Bitmap Extended"								],
	[ "66",		"",				"N",			 "1",		"Settlement Code"								],
	[ "67",		"",				"N",			 "2",		"Extended Payment Code"							],
	[ "68",		"",				"N",			 "3",		"Receiving Institution Country Code"			],
	[ "69",		"",				"N",			 "3",		"Settlement Institution Country Code"			],
	[ "70",		"",				"N",			 "3",		"Network Management Information Code"			],
	[ "71",		"",				"N",			 "4",		"Message Number"								],
	[ "72",		"LLLVAR",		"N",		  "...4",		"Message Last Number"							],
	[ "73",		"YYMMDD",		"N",			 "6",		"Date Action"									],
	[ "74",		"",				"N",			"10",		"Credits Number"								],
	[ "75",		"",				"N",			"10",		"Credit Reversals Number"						],
	[ "76",		"",				"N",			"10",		"Debits Action"									],
	[ "77",		"",				"N",			"10",		"Debit Reversals Number"						],
	[ "78",		"",				"N",			"10",		"Transfer Action"								],
	[ "79",		"",				"N",			"10",		"Transfer Reversals Number"						],
	[ "80",		"",				"N",			"10",		"Inquiries Number"								],
	[ "81",		"",				"N",			"10",		"Authorization Amount"							],
	[ "82",		"",				"N",			"12",		"Credits Processing Fee Amount"					],
	[ "83",		"",				"N",			"12",		"Credits Transaction Fee Amount"				],
	[ "84",		"",				"N",			"12",		"Debits Processing Fee Amount"					],
	[ "85",		"",				"N",			"12",		"Debits Transaction Fee Amount"					],
	[ "86",		"",				"N",			"15",		"Credits Amount"								],
	[ "87",		"",				"N",			"15",		"Credit Reversal Amount"						],
	[ "88",		"",				"N",			"15",		"Debits Amount"									],
	[ "89",		"",				"N",			"15",		"Debit Reversals Amount"						],
	[ "90",		"",				"N",			"42",		"Original Data Elements"						],
	[ "91",		"",			   "AN",			 "1",		"File Update Code"								],
	[ "92",		"",				"N",			 "2",		"File Security Code"							],
	[ "93",		"",				"N",			 "5",		"Response Indicator"							],
	[ "94",		"",			   "AN",			 "7",		"Service Indicator"								],
	[ "95",		"",			   "AN",			"42",		"Replacement Amounts"							],
	[ "96",		"",			   "AN",			 "8",		"Message Security Code"							],
	[ "97",		"",				"N",			"16",		"Amount Net Settlement"							],
	[ "98",		"",			  "ANS",			"25",		"Payee"											],
	[ "99",		"LLVAR",		"N",		  "..11",		"Settlement Institution Identification Code"	],
	[ "100",	"LLVAR",		"N",		  "..11",		"Receiving Institution Identification Code"		],
	[ "101",	"",			  "ANS",			"17",		"Filename"										],
	[ "102",	"LLVAR",	  "ANS",		  "..28",		"Account Identification"						],
	[ "103",	"LLVAR",	  "ANS",		  "..28",		"Account Identification"						],
	[ "104",	"LLLVAR",     "ANS",		"...100",		"Transaction Description"						],
	[ "105",	"LLLVAR",     "ANS",		"...999",		"Reserved For ISO Use"							],
	[ "106",	"LLLVAR",     "ANS",		"...999",		"Reserved For ISO Use"							],
	[ "107",	"LLLVAR",     "ANS",		"...999",		"Reserved For ISO Use"							],
	[ "108",	"LLLVAR",     "ANS",		"...999",		"Reserved For ISO Use"							],
	[ "109",	"LLLVAR",     "ANS",		"...999",		"Reserved For ISO Use"							],
	[ "110",	"LLLVAR",     "ANS",		"...999",		"Reserved For ISO Use"							],
	[ "111",	"LLLVAR",     "ANS",		"...999",		"Reserved For ISO Use"							],
	[ "112",	"LLLVAR",     "ANS",		"...999",		"Reserved For National Use"						],
	[ "113",	"LLVAR",		"N",		  "..11",		"Reserved For National Use"						],
	[ "114",	"LLLVAR",     "ANS",		"...999",		"Reserved For National Use"						],
	[ "115",	"LLLVAR",     "ANS",		"...999",		"Reserved For National Use"						],
	[ "116",	"LLLVAR",     "ANS",		"...999",		"Reserved For National Use"						],
	[ "117",	"LLLVAR",     "ANS",		 "..999",		"Card Status Update Code (AUS Only)"			],
	[ "118",	"LLLVAR",     "ANS",		"...999",		"Cash Total Number (AUS Only)"					],
	[ "119",	"LLLVAR",     "ANS",		"...999",		"Cash Total Amount (AUS Only)"					],
	[ "120",	"LLLVAR",     "ANS",		"...999",		"Reserved For Private Use"						],
	[ "121",	"LLLVAR",     "ANS",		"...999",		"Reserved For Private Use"						],
	[ "122",	"LLLVAR",     "ANS",		"...999",		"Reserved For Private Use"						],
	[ "123",	"LLLVAR",     "ANS",		"...999",		"Reserved For Private Use"						],
	[ "124",	"LLLVAR",     "ANS",		"...255",		"Reserved For Private Use"						],
	[ "125",	"LLVAR",	  "ANS",		  "..50",		"Reserved For Private Use"						],
	[ "126",	"LLLVAR",     "ANS",		"...999",		"Reserved For Private Use"						],
	[ "127",	"LLLVAR",     "ANS",		"...999",		"Reserved For Private Use"						],
	[ "128",	"",				"B",			"16",		"Message Authentication Code"					]
]


class Handler:
	def onWindowDestroy(self, *args):
		Gtk.main_quit(*args)

	def onToggledButton1(self, widget):
		radio = builder.get_object("radiobutton1")
		alignment = builder.get_object("alignment2")
		alignment.set_sensitive(not radio.get_active());

	def onToggledButton2(self, widget):
		radio = builder.get_object("radiobutton2")
		alignment = builder.get_object("alignment1")
		alignment.set_sensitive(not radio.get_active());

	def onTextChange(self, widget):
		pos = 0
		radio = builder.get_object("radiobutton1")

		if radio.get_active():
			store = builder.get_object("liststore1");
			store.clear();
			"""
			h = "%s" % widget.get_text()
			num = int(h, 16)
			text = "%02X" % num
			widget.set_text(text)
			"""

			for i in range(1, 128):
				cb = "checkbutton%d" % i
				check = builder.get_object(cb)
				check.set_active(False)

			pos = 0

			for i in range(0, 16):
				epos = (i + 1)
				e = "entry%s" % epos
				entry = builder.get_object(e)
				h = "%s" % entry.get_text()
				num = int(h, 16)
				x = 8 * (epos - 1)

				#if entry.get_text() != "00":
				for j in range(0, 8):
					pos = ((j + 1) + x)
					cb = "checkbutton%d" % pos
					check = builder.get_object(cb)

					if bool(num & bits[j]):
						check.set_active(True)
						store.append(bitmap[pos-1]);

	def onButtonChecked(self, widget):
		radio = builder.get_object("radiobutton2")

		if radio.get_active():
			store = builder.get_object("liststore1");
			store.clear();

			for i in range(0, 16):
				epos = (i + 1)
				e = "entry%s" % epos
				entry = builder.get_object(e)
				x = 8 * (epos - 1)
				bit = 0

				for j in range(0, 8):
					pos = ((j + 1) + x)
					cb = "checkbutton%d" % pos
					check = builder.get_object(cb)

					if check.get_active():
						bit |= bits[j]
						store.append(bitmap[pos-1]);
						
						if pos > 64:
							cb1 = "checkbutton1"
							checkBit1 = builder.get_object(cb1)
							checkBit1.set_active(True)

				hexa = "%02X" % bit
				entry.set_text(hexa)

class ISO8583App(object):
	def __init__(self):
		#builder = Gtk.Builder()
		builder.add_from_file("./iso8583-bitmap.glade")
		builder.connect_signals(Handler())

		window = builder.get_object("window")
		window.show_all()

		Gtk.main()

if __name__ == "__main__":
	app = ISO8583App()
