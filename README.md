# EG244-Lab-3
EG244 -  Group project

Idea(1):  The Delivery

* You are a courier trying to deliver a package to a Mr.Samsa’s office at the Rigid-works building.

* You go to the reception and tell the receptionist you have a package for Mr.Samsa, he tells you you need a an item from security to verify that the package is meant for Mr.Samsa since he is not in today, you will receive a silver chip from security.

* You go through the atrium to get to the security room, here you’ll meet an officer that says you first have to, provide a filled delivery form, you have to goto Arrivals.

* As you try an deliver,  you find out that the company is currently researching
  Methods of teleportation, you find a faulty teleportation room that randomly teleports you to a room in the facility, to access it you need to be in the laboratory (There is a locked exit in the room, in)

*

* To win the game complete the delivery 

Rooms

 Reception 
 
	Exits : West - Atrium; East - Hallway
	Items:

 East Hallway 
 
	Exits : East - Reception; West - Restroom; North - Arrivals
	Items:

 Arrivals 
 
	Exits : South - East Hallway; East - Teleportation RD Lab
	Items:

 Restroom  
 
	Exits : East - East Hallway
	Items:

 Atrium 
 
	Exits : Reception - East; North - Security Room; West - Hallway; South - Cafeteria
	Items:

 Security Room
 
	Exits : South: Atrium
	Items:

 West Hallway 
 
	Exits : East - Atrium; North - Marketing Offices; West - Restroom
	Items:

 Cafeteria  
 
	Exit : North - Atrium;
	Items:

 Restroom  
 
	Exits : South - West Hallway
	Items:

 Teleportation R&D Lab 
 
	Exit : North - FET; West - Arrivals; East - Locked Equipment Closet
	Items:

 Equipment Storage  
 
	Exit : West - Lab
	Items:

 Faulty Experimental Teleportation room  
 
	Exit:  ????
	Items:

 Marketing Offices 
 
	Exits : East - West Hallway; North - Mr.Samsa Office (Locked
	Items:

 Mr.Samsa’s Office
 
	Exits :  South - Marketing
	Items:

Items

Silver chip : Key 

	Allows the player to deliver the package at the reception when handed to receptionist
	Description : Silver RFID Chip
	Location : Security Room (Security Officer)
	Weight : 0.05

Delivery Form : Key 

	Allows the player to get the the silver chip from the security room
	Description : Document with details of the delivery and package.
	Location : Arrivals (Clerk); 
	Weight : 0.01

Experimental Serum U - 56 : Consumable;

	Description : Glass container with neon blue liquid
	Effect : 1 in 50 chance of teleporting the player to Mr.Samsa’s office to deliver	Location :  Teleportation Lab; 
	Weight : 0.5

Experimental Serum U - 69 : Consumable;

	 Description : Glass container with 
	 Effect : 1 in 10 chance of reducing coordination i.e. interpreting commands incorrectly or  1 in 1000 chance of fatality.
	 Location : Teleportation Lab
	 Weight : 0.7

Prototype Teleporter : Teleporter;

	Description : Can be used to teleport anywhere in the building. Has a small LCD screen.
	Location : Equipment closet; 
	Weight : 2.5

Blue Keycard : Key; 

	Description : Unlocks the equipment closet;
	Location : Restroom 
	Weight : 0.1.

Red Keycard : Key;

	Description : Unlocks Composite Lab Maintenance closet; 
	Location : Cafeteria
	Weight : 0.1

Teal Keycard : Key;

	Description : Dr. Hsu’s keycard 
	Location : Restroom
	Weight : 0.1

Box : Item; 

	(Filler)
	Location
	Weight > 4

Package : Key; 

	Description : Addressed for a Mr.Samsa at Rigid-Works, 917 Administration Ave, Arkansas
	Location : Player Inventory 
	Weight : 2.5.


Characters

Receptionist  

	Description: can receive package to win game
	Location:
	Items:

Officer David 

	Description: Deals with security in the building
	Location:
	Items:

Mr.Smith 

	Description: Lab Technician
	Location:
	Items:

Rudy 

	Description: Custodial worker
	Location:

Dr.Hay 

	Description: Works in Teleportation RD
	Location:
	Items:

Dr. Solis 

	Description: Works in Teleportation RD
	Location:
	Items:

Ms. Chungu 

	Description: Lab Technician
	Location:
	Items:

Dr. Hsu 
	Can give you access to Teleportation RD as long as you give find his keycard

	Description: Works in Teleportation RD. 
	Location:
	Items :
	
