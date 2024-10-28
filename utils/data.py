# -------------------------------------------------------------------------------------------------------
# File Name: data.py
# Author:   Jai Verma
# Description: A file for storing variables / data that is repeatedly used throughout the project.
# -------------------------------------------------------------------------------------------------------

SEASONS = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018,
            2019, 2020, 2021, 2022, 2023, 2024]


TEAMS = ['Royal Challengers Bangalore', 'Punjab Kings', 'Delhi Capitals',
       'Mumbai Indians', 'Kolkata Knight Riders', 'Rajasthan Royals',
       'Deccan Chargers', 'Chennai Super Kings', 'Kochi Tuskers Kerala',
       'Pune Warriors', 'Sunrisers Hyderabad', 'Gujarat Lions',
       'Rising Pune Supergiants', 'Lucknow Super Giants',
       'Gujarat Titans']

STADIUMS = ['M Chinnaswamy Stadium', 'Punjab Cricket Association Stadium',
       'Feroz Shah Kotla', 'Wankhede Stadium', 'Eden Gardens',
       'Sawai Mansingh Stadium', 'Rajiv Gandhi International Stadium',
       'MA Chidambaram Stadium', 'Dr DY Patil Sports Academy', 'Newlands',
       "St George's Park", 'Kingsmead', 'SuperSport Park', 'Buffalo Park',
       'New Wanderers Stadium', 'De Beers Diamond Oval',
       'OUTsurance Oval', 'Brabourne Stadium',
       'Sardar Patel Stadium, Motera', 'Barabati Stadium',
       'Vidarbha Cricket Association Stadium, Jamtha',
       'Himachal Pradesh Cricket Association Stadium', 'Nehru Stadium',
       'Holkar Cricket Stadium',
       'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium',
       'Subrata Roy Sahara Stadium',
       'Maharashtra Cricket Association Stadium',
       'Shaheed Veer Narayan Singh International Stadium',
       'JSCA International Stadium Complex', 'Sheikh Zayed Stadium',
       'Sharjah Cricket Stadium', 'Dubai International Cricket Stadium',
       'Saurashtra Cricket Association Stadium', 'Green Park',
       'Arun Jaitley Stadium', 'Narendra Modi Stadium, Ahmedabad',
       'Zayed Cricket Stadium, Abu Dhabi',
       'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow',
       'Barsapara Cricket Stadium, Guwahati',
       'Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur']

PLAYERS = ['A Ashish Reddy', 'A Badoni', 'A Chandila', 'A Chopra',
       'A Choudhary', 'A Dananjaya', 'A Flintoff', 'A Kamboj', 'A Kumble',
       'A Manohar', 'A Mishra', 'A Mithun', 'A Mukund', 'A Nehra',
       'A Nel', 'A Nortje', 'A Raghuvanshi', 'A Singh', 'A Symonds',
       'A Tomar', 'A Uniyal', 'A Zampa', 'AA Bilakhia', 'AA Chavan',
       'AA Jhunjhunwala', 'AA Kazi', 'AA Kulkarni', 'AA Noffke',
       'AB Agarkar', 'AB Barath', 'AB Dinda', 'AB McDonald',
       'AB de Villiers', 'AC Blizzard', 'AC Gilchrist', 'AC Thomas',
       'AC Voges', 'AD Hales', 'AD Mascarenhas', 'AD Mathews', 'AD Nath',
       'AD Russell', 'AF Milne', 'AG Murtaza', 'AG Paunikar', 'AJ Finch',
       'AJ Hosein', 'AJ Turner', 'AJ Tye', 'AK Markram', 'AL Menaria',
       'AM Nayar', 'AM Rahane', 'AM Salvi', 'AN Ahmed', 'AN Ghosh',
       'AP Dole', 'AP Majumdar', 'AP Tare', 'AR Bawne', 'AR Patel',
       'AS Joseph', 'AS Rajpoot', 'AS Raut', 'AS Roy', 'AS Yadav',
       'AT Carey', 'AT Rayudu', 'AU Rashid', 'AUK Pathan', 'AV Wankhade',
       'Abdul Basith', 'Abdul Samad', 'Abdur Razzak', 'Abhishek Sharma',
       'Abishek Porel', 'Akash Deep', 'Akash Madhwal', 'Akash Singh',
       'Aman Hakim Khan', 'Anand Rajan', 'Anirudh Singh', 'Ankit Sharma',
       'Ankit Soni', 'Anmolpreet Singh', 'Anuj Rawat', 'Anureet Singh',
       'Arjun Tendulkar', 'Arshad Khan', 'Arshad Khan (2)',
       'Arshdeep Singh', 'Ashutosh Sharma', 'Atharva Taide', 'Avesh Khan',
       'Azhar Mahmood', 'Azmatullah Omarzai', 'B Akhil', 'B Aparajith',
       'B Chipli', 'B Geeves', 'B Indrajith', 'B Kumar', 'B Laughlin',
       'B Lee', 'B Sai Sudharsan', 'B Stanlake', 'B Sumanth', 'BA Bhatt',
       'BA Stokes', 'BAW Mendis', 'BB McCullum', 'BB Samantray',
       'BB Sran', 'BCJ Cutting', 'BE Hendricks', 'BJ Haddin', 'BJ Hodge',
       'BJ Rohrer', 'BMAJ Mendis', 'BR Dunk', 'BR Sharath',
       'BW Hilfenhaus', 'Basil Thampi', 'Bipul Sharma', 'C Ganapathy',
       'C Green', 'C Madan', 'C Munro', 'C Nanda', 'C Sakariya',
       'C de Grandhomme', 'CA Ingram', 'CA Lynn', 'CA Pujara', 'CH Gayle',
       'CH Morris', 'CJ Anderson', 'CJ Dala', 'CJ Ferguson', 'CJ Green',
       'CJ Jordan', 'CJ McKay', 'CK Kapugedera', 'CK Langeveldt',
       'CL White', 'CM Gautam', 'CR Brathwaite', 'CR Woakes',
       'CRD Fernando', 'CV Varun', 'D Brevis', 'D Ferreira', 'D Jansen',
       'D Kalyankrishna', 'D Padikkal', 'D Pretorius', 'D Salunkhe',
       'D Wiese', 'D du Preez', 'DA Miller', 'DA Warner', 'DAJ Bracewell',
       'DB Das', 'DB Ravi Teja', 'DE Bollinger', 'DG Nalkande',
       'DH Yagnik', 'DJ Bravo', 'DJ Harris', 'DJ Hooda', 'DJ Hussey',
       'DJ Jacobs', 'DJ Malan', 'DJ Mitchell', 'DJ Muthuswami',
       'DJ Thornely', 'DJ Willey', 'DJG Sammy', 'DJM Short', 'DL Chahar',
       'DL Vettori', 'DM Bravo', 'DNT Zoysa', 'DP Conway', 'DP Nannes',
       'DP Vijaykumar', 'DPMD Jayawardene', 'DR Martyn', 'DR Sams',
       'DR Shorey', 'DR Smith', 'DS Kulkarni', 'DS Lehmann',
       'DT Christian', 'DT Patil', 'DW Steyn', 'Dhruv Jurel', 'E Lewis',
       'EJG Morgan', 'ER Dwivedi', 'F Behardien', 'F du Plessis',
       'FA Allen', 'FH Edwards', 'FY Fazal', 'Fazalhaq Farooqi',
       'G Coetzee', 'G Gambhir', 'GB Hogg', 'GC Smith', 'GC Viljoen',
       'GD McGrath', 'GD Phillips', 'GH Vihari', 'GHS Garton',
       'GJ Bailey', 'GJ Maxwell', 'GR Napier', 'GS Sandhu',
       'Gagandeep Singh', 'Gulbadin Naib', 'Gurkeerat Singh',
       'Gurnoor Brar', 'H Das', 'H Klaasen', 'H Sharma', 'HC Brook',
       'HE van der Dussen', 'HF Gurney', 'HH Gibbs', 'HH Pandya',
       'HM Amla', 'HR Shokeen', 'HV Patel', 'Harbhajan Singh',
       'Harmeet Singh', 'Harpreet Brar', 'Harpreet Singh', 'Harshit Rana',
       'I Malhotra', 'I Sharma', 'I Udana', 'IC Pandey', 'IC Porel',
       'IK Pathan', 'IR Jaggi', 'IS Sodhi', 'Imran Tahir',
       'Iqbal Abdulla', 'Ishan Kishan', 'J Arunkumar', 'J Botha',
       'J Fraser-McGurk', 'J Little', 'J Suchith', 'J Syed Mohammad',
       'J Theron', 'J Yadav', 'JA Morkel', 'JA Richardson', 'JC Archer',
       'JC Buttler', 'JD Ryder', 'JD Unadkat', 'JDP Oram', 'JDS Neesham',
       'JE Root', 'JE Taylor', 'JEC Franklin', 'JH Kallis', 'JJ Bumrah',
       'JJ Roy', 'JJ van der Wath', 'JL Denly', 'JL Pattinson',
       'JM Bairstow', 'JM Kemp', 'JM Sharma', 'JO Holder',
       'JP Behrendorff', 'JP Duminy', 'JP Faulkner',
       'JPR Scantlebury-Searles', 'JR Hazlewood', 'JR Hopes',
       'JR Philippe', 'JW Hastings', 'Jalaj S Saxena', 'Jaskaran Singh',
       'Joginder Sharma', 'K Goel', 'K Gowtham', 'K Kartikeya',
       'K Khejroliya', 'K Rabada', 'K Santokie', 'K Upadhyay', 'K Yadav',
       'KA Jamieson', 'KA Maharaj', 'KA Pollard', 'KAJ Roach',
       'KB Arun Karthik', 'KC Cariappa', 'KC Sangakkara', 'KD Karthik',
       'KH Devdhar', 'KH Pandya', 'KJ Abbott', 'KK Ahmed', 'KK Cooper',
       'KK Nair', 'KL Nagarkoti', 'KL Rahul', 'KM Asif', 'KM Jadhav',
       'KMA Paul', 'KMDN Kulasekara', 'KP Appanna', 'KP Pietersen',
       'KR Mayers', 'KR Sen', 'KS Bharat', 'KS Sharma', 'KS Williamson',
       'KT Maphaka', 'KV Sharma', 'KW Richardson', 'Kamran Akmal',
       'Kamran Khan', 'Karanveer Singh', 'Kartik Tyagi', 'Kuldeep Yadav',
       'Kumar Kushagra', 'L Ablish', 'L Balaji', 'L Ngidi', 'L Ronchi',
       'L Wood', 'LA Carseldine', 'LA Pomersbach', 'LB Williams',
       'LE Plunkett', 'LH Ferguson', 'LI Meriwala', 'LJ Wright',
       'LMP Simmons', 'LPC Silva', 'LR Shukla', 'LRPL Taylor',
       'LS Livingstone', 'Lalit Yadav', 'Liton Das', 'M Ashwin',
       'M Jansen', 'M Kaif', 'M Kartik', 'M Klinger', 'M Manhas',
       'M Markande', 'M Morkel', 'M Muralitharan', 'M Ntini',
       'M Pathirana', 'M Prasidh Krishna', 'M Rawat', 'M Shahrukh Khan',
       'M Siddharth', 'M Theekshana', 'M Vijay', 'M Vohra', 'M de Lange',
       'MA Agarwal', 'MA Khote', 'MA Starc', 'MA Wood', 'MB Parmar',
       'MC Henriques', 'MC Juneja', 'MD Mishra', 'MD Shanaka',
       'MDKJ Perera', 'MEK Hussey', 'MF Maharoof', 'MG Bracewell',
       'MG Johnson', 'MG Neser', 'MJ Clarke', 'MJ Guptill', 'MJ Henry',
       'MJ Lumb', 'MJ McClenaghan', 'MJ Santner', 'MJ Suthar',
       'MK Lomror', 'MK Pandey', 'MK Tiwary', 'ML Hayden', 'MM Ali',
       'MM Patel', 'MM Sharma', 'MN Samuels', 'MN van Wyk', 'MP Stoinis',
       'MP Yadav', 'MR Marsh', 'MS Bisla', 'MS Dhoni', 'MS Gony',
       'MS Wade', 'MV Boucher', 'MW Short', 'Mandeep Singh',
       'Mashrafe Mortaza', 'Mayank Dagar', 'Milind Kumar',
       'Misbah-ul-Haq', 'Mohammad Ashraful', 'Mohammad Asif',
       'Mohammad Hafeez', 'Mohammad Nabi', 'Mohammed Shami',
       'Mohammed Siraj', 'Mohit Rathee', 'Mohsin Khan', 'Monu Kumar',
       'Mujeeb Ur Rahman', 'Mukesh Choudhary', 'Mukesh Kumar',
       'Mustafizur Rahman', 'N Burger', 'N Jagadeesan', 'N Pooran',
       'N Rana', 'N Saini', 'N Thushara', 'N Wadhera', 'NA Saini',
       'NB Singh', 'ND Doshi', 'NJ Maddinson', 'NJ Rimmington',
       'NK Patel', 'NL McCullum', 'NLTC Perera', 'NM Coulter-Nile',
       'NS Naik', 'NT Ellis', 'NV Ojha', 'Naman Dhir', 'Navdeep Saini',
       'Naveen-ul-Haq', 'Nithish Kumar Reddy', 'Noor Ahmad', 'O Thomas',
       'OA Shah', 'OC McCoy', 'OF Smith', 'P Amarnath', 'P Awana',
       'P Chopra', 'P Dogra', 'P Dubey', 'P Kumar', 'P Negi',
       'P Parameswaran', 'P Prasanth', 'P Ray Barman', 'P Sahu',
       'P Simran Singh', 'P Suyal', 'PA Patel', 'PA Reddy',
       'PBB Rajapaksa', 'PC Valthaty', 'PD Collingwood', 'PD Salt',
       'PH Solanki', 'PJ Cummins', 'PJ Sangwan', 'PK Garg',
       'PM Sarvesh Kumar', 'PN Mankad', 'PP Chawla', 'PP Ojha', 'PP Shaw',
       'PR Shah', 'PSP Handscomb', 'PV Tambe', 'PVD Chameera',
       'PWH de Silva', 'Pankaj Singh', 'Parvez Rasool', 'Q de Kock',
       'R Ashwin', 'R Bhatia', 'R Bishnoi', 'R Dhawan', 'R Dravid',
       'R Goyal', 'R McLaren', 'R Ninan', 'R Parag', 'R Powell',
       'R Rampaul', 'R Ravindra', 'R Sai Kishore', 'R Sanjay Yadav',
       'R Sathish', 'R Sharma', 'R Shepherd', 'R Shukla', 'R Tewatia',
       'R Vinay Kumar', 'RA Bawa', 'RA Jadeja', 'RA Shaikh',
       'RA Tripathi', 'RD Chahar', 'RD Gaikwad', 'RE Levi',
       'RE van der Merwe', 'RG More', 'RG Sharma', 'RJ Gleeson',
       'RJ Harris', 'RJ Peterson', 'RJ Quiney', 'RJW Topley', 'RK Bhui',
       'RK Singh', 'RM Patidar', 'RN ten Doeschate', 'RP Meredith',
       'RP Singh', 'RR Bhatkal', 'RR Bose', 'RR Pant', 'RR Powar',
       'RR Raje', 'RR Rossouw', 'RR Sarwan', 'RS Bopara', 'RS Gavaskar',
       'RS Hangargekar', 'RS Sodhi', 'RT Ponting', 'RV Gomez', 'RV Patel',
       'RV Uthappa', 'RW Price', 'Rahmanullah Gurbaz', 'Ramandeep Singh',
       'Rashid Khan', 'Rasikh Salam', 'Ravi Bishnoi', 'S Anirudha',
       'S Aravind', 'S Badree', 'S Badrinath', 'S Chanderpaul',
       'S Dhawan', 'S Dube', 'S Gopal', 'S Joseph', 'S Kaul', 'S Kaushik',
       'S Ladda', 'S Lamichhane', 'S Midhun', 'S Nadeem', 'S Narwal',
       'S Rana', 'S Randiv', 'S Sandeep Warrier', 'S Sohal',
       'S Sreesanth', 'S Sriram', 'S Tyagi', 'S Vidyut', 'SA Abbott',
       'SA Asnodkar', 'SA Yadav', 'SB Bangar', 'SB Dubey', 'SB Jakati',
       'SB Joshi', 'SB Styris', 'SB Wagh', 'SC Ganguly', 'SC Kuggeleijn',
       'SD Chitnis', 'SD Hope', 'SD Lad', 'SE Bond', 'SE Marsh',
       'SE Rutherford', 'SH Johnson', 'SJ Srivastava', 'SK Raina',
       'SK Rasheed', 'SK Trivedi', 'SK Warne', 'SL Malinga', 'SM Boland',
       'SM Curran', 'SM Harwood', 'SM Katich', 'SM Pollock',
       'SMSM Senanayake', 'SN Khan', 'SN Thakur', 'SO Hetmyer',
       'SP Fleming', 'SP Goswami', 'SP Jackson', 'SP Narine', 'SPD Smith',
       'SR Tendulkar', 'SR Watson', 'SS Agarwal', 'SS Cottrell',
       'SS Iyer', 'SS Mundhe', 'SS Prabhudessai', 'SS Sarkar',
       'SS Shaikh', 'SS Tiwary', 'SSB Magala', 'ST Jayasuriya',
       'STR Binny', 'SV Samson', 'SW Billings', 'SW Tait', 'SZ Mulani',
       'Sachin Baby', 'Salman Butt', 'Sameer Rizvi', 'Sandeep Sharma',
       'Sanvir Singh', 'Saurav Chauhan', 'Shahbaz Ahmed', 'Shahid Afridi',
       'Shakib Al Hasan', 'Shashank Singh', 'Shivam Mavi',
       'Shivam Sharma', 'Shivam Singh', 'Shoaib Ahmed', 'Shoaib Akhtar',
       'Shoaib Malik', 'Shubman Gill', 'Sikandar Raza', 'Simarjeet Singh',
       'Sohail Tanvir', 'Sonu Yadav', 'Subhransu Senapati', 'Sumit Kumar',
       'Sunny Gupta', 'Sunny Singh', 'Suyash Sharma', 'Swapnil Singh',
       'T Banton', 'T Henderson', 'T Kohler-Cadmore', 'T Kohli',
       'T Mishra', 'T Natarajan', 'T Shamsi', 'T Stubbs', 'T Taibu',
       'T Thushara', 'TA Boult', 'TD Paine', 'TG Southee', 'TH David',
       'TK Curran', 'TL Seifert', 'TL Suman', 'TM Dilshan', 'TM Head',
       'TM Srivastava', 'TP Sudhindra', 'TR Birt', 'TS Mills',
       'TU Deshpande', 'Tanay Thyagarajan', 'Tanush Kotian',
       'Tejas Baroka', 'Tilak Varma', 'U Kaul', 'UA Birla', 'UBT Chand',
       'UT Khawaja', 'UT Yadav', 'Umar Gul', 'Umran Malik', 'V Kaverappa',
       'V Kohli', 'V Pratap Singh', 'V Sehwag', 'V Shankar',
       'V Viyaskanth', 'VG Arora', 'VH Zol', 'VR Aaron', 'VR Iyer',
       'VRV Singh', 'VS Malik', 'VS Yeligati', 'VVS Laxman', 'VY Mahesh',
       'Vijaykumar Vyshak', 'Virat Singh', 'Vishnu Vinod',
       'Vivrant Sharma', 'W Jaffer', 'WA Mota', 'WD Parnell', 'WG Jacks',
       'WP Saha', 'WPUJC Vaas', 'Washington Sundar',
       'X Thalaivan Sargunam', 'Y Gnaneswara Rao', 'Y Nagar',
       'Y Prithvi Raj', 'Y Venugopal Rao', 'YA Abdulla', 'YBK Jaiswal',
       'YK Pathan', 'YS Chahal', 'YV Dhull', 'YV Takawale', 'Yash Dayal',
       'Yash Thakur', 'Yashpal Singh', 'Younis Khan', 'Yudhvir Singh',
       'Yuvraj Singh', 'Z Khan']