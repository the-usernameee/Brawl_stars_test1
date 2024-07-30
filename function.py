def func(x,fl):
	tr0="game_assets/for_tier/ok.png"
	tr1_u,tr1_d="game_assets/for_tier/aaa/one_u.png","game_assets/for_tier/aaa/one_d.png"
	tr2_u,tr2_d="game_assets/for_tier/aaa/two_u.png","game_assets/for_tier/aaa/two_d.png"
	tr3_u,tr3_d="game_assets/for_tier/aaa/three_u.png","game_assets/for_tier/aaa/three_d.png"
	tr4_u,tr4_d="game_assets/for_tier/aaa/four_u.png","game_assets/for_tier/aaa/four_d.png"
	tr5_u,tr5_d="game_assets/for_tier/aaa/five_u.png","game_assets/for_tier/aaa/five_d.png"
	
	lg0="game_assets/for_tier/ok.png"
	lg1_up,lg1_dn="game_assets/for_tier/trophy_tiers/woody_u.png","game_assets/for_tier/trophy_tiers/woody_d.png"
	lg2_up,lg2_dn="game_assets/for_tier/trophy_tiers/bronze_u.png","game_assets/for_tier/trophy_tiers/bronze_d.png"
	lg3_up,lg3_dn="game_assets/for_tier/trophy_tiers/silver_u.png","game_assets/for_tier/trophy_tiers/silver_d.png"
	lg4_up,lg4_dn="game_assets/for_tier/trophy_tiers/gold_u.png","game_assets/for_tier/trophy_tiers/gold_d.png"
	lg5_up,lg5_dn="game_assets/for_tier/trophy_tiers/diamond_u.png","game_assets/for_tier/trophy_tiers/diamond_d.png"
	lg6_up,lg6_dn="game_assets/for_tier/trophy_tiers/epic_u.png","game_assets/for_tier/trophy_tiers/epic_d.png"
	lg7_up,lg7_dn="game_assets/for_tier/trophy_tiers/mythic_u.png","game_assets/for_tier/trophy_tiers/mythic_d.png"
	lg8_up,lg8_dn="game_assets/for_tier/trophy_tiers/t1_u.png","game_assets/for_tier/trophy_tiers/t1_d.png"
	lg9_up,lg9_dn="game_assets/for_tier/trophy_tiers/t2_u.png","game_assets/for_tier/trophy_tiers/t2_d.png"
	lg10_up,lg10_dn="game_assets/for_tier/trophy_tiers/t3_u.png","game_assets/for_tier/trophy_tiers/t3_d.png"
	lg11_up,lg11_dn="game_assets/for_tier/trophy_tiers/t4_u.png","game_assets/for_tier/trophy_tiers/t4_d.png"	
	GG=((500,((lg0,tr0),(lg0,tr0))),
	  
	(650,((lg1_up,tr1_u),(lg1_dn,tr1_d))),
	(800,((lg1_up,tr2_u),(lg1_dn,tr2_d))),
	(1000,((lg1_up,tr3_d),(lg1_dn,tr3_d))),
	
	(1300,((lg2_up,tr1_u),(lg2_dn,tr1_d))),
	(1600,((lg2_up,tr2_u),(lg2_dn,tr2_d))),
	(2000,((lg2_up,tr3_u),(lg2_dn,tr3_d))),
	
	(2300,((lg3_up,tr1_u),(lg3_dn,tr1_d))),
	(2600,((lg3_up,tr2_u),(lg3_dn,tr2_d))),
	(3000,((lg3_up,tr3_u),(lg3_dn,tr3_d))),
	
	(3300,((lg4_up,tr1_u),(lg4_dn,tr1_d))),
	(3600,((lg4_up,tr2_u),(lg4_dn,tr2_d))),
	(4000,((lg4_up,tr3_u),(lg4_dn,tr3_d))),
	
	(4500,((lg5_up,tr1_u),(lg5_dn,tr1_d))),
	(5000,((lg5_up,tr2_u),(lg5_dn,tr2_d))),
	(5500,((lg5_up,tr3_u),(lg5_dn,tr3_d))),
	(6000,((lg5_up,tr4_u),(lg5_dn,tr4_d))),
		
	(6500,((lg6_up,tr1_u),(lg6_dn,tr1_d))),
	(7000,((lg6_up,tr2_u),(lg6_dn,tr2_d))),
	(7500,((lg6_up,tr3_u),(lg6_dn,tr3_d))),
	(8000,((lg6_up,tr4_u),(lg6_dn,tr4_d))),
	
	(8500,((lg7_up,tr1_u),(lg7_dn,tr1_d))),
	(9000,((lg7_up,tr2_u),(lg7_dn,tr2_d))),
	(9500,((lg7_up,tr3_u),(lg7_dn,tr3_d))),
	(10000,((lg7_up,tr4_u),(lg7_dn,tr4_d))),
	
	(11000,((lg8_up,tr1_u),(lg8_dn,tr1_d))),
	(12000,((lg8_up,tr2_u),(lg8_dn,tr2_d))),
	(13000,((lg8_up,tr3_u),(lg8_dn,tr3_d))),
	(14000,((lg8_up,tr4_u),(lg8_dn,tr4_d))),
	(16000,((lg8_up,tr5_u),(lg8_dn,tr5_d))),
	
	(18000,((lg9_up,tr1_u),(lg9_dn,tr1_d))),
	(20000,((lg9_up,tr2_u),(lg9_dn,tr2_d))),
	(22000,((lg9_up,tr3_u),(lg9_dn,tr3_d))),
	(25000,((lg9_up,tr4_u),(lg9_dn,tr4_d))),
	(30000,((lg9_up,tr5_u),(lg9_dn,tr5_d))),
	
	(35000,((lg10_up,tr1_u),(lg10_dn,tr1_d))),
	(40000,((lg10_up,tr2_u),(lg10_dn,tr2_d))),
	(45000,((lg10_up,tr3_u),(lg10_dn,tr3_d))),
	(50000,((lg10_up,tr4_u),(lg10_dn,tr4_d))),
	(55000,((lg10_up,tr5_u),(lg10_dn,tr5_d))),
	
	(60000,((lg11_up,tr1_u),(lg11_dn,tr1_d))),
	(65000,((lg11_up,tr2_u),(lg11_dn,tr2_d))),
	(70000,((lg11_up,tr3_u),(lg11_dn,tr3_d))),
	(float("inf"),((lg11_up,tr4_u),(lg11_dn,tr4_d)))
	)
	for g in GG:
		if int(x)<g[0]:
			return g[1][fl]