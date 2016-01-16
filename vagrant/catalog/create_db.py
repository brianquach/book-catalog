from catalog import db
from catalog.models import Catagory, CatagoryItem

# Create database schema
db.create_all()

# Create and add default catagories (book genres)
animal = Catagory(name='Animal')
db.session.add(animal)
art = Catagory(name='Art')
db.session.add(art)
autobiography = Catagory(name='Autobiography')
db.session.add(autobiography)
biography = Catagory(name='Biography')
db.session.add(biography)
business = Catagory(name='Business')
db.session.add(business)
children = Catagory(name='Children')
db.session.add(children)
classics = Catagory(name='Classics')
db.session.add(classics)
comedy = Catagory(name='Comedy')
db.session.add(comedy)
comic = Catagory(name='Comic')
db.session.add(comic)
computing = Catagory(name='Computing')
db.session.add(computing)
culture = Catagory(name='Culture')
db.session.add(culture)
education = Catagory(name='Education')
db.session.add(education)
fantasy = Catagory(name='Fantasy')
db.session.add(fantasy)
fiction = Catagory(name='Fiction')
db.session.add(fiction)
finance = Catagory(name='Finance')
db.session.add(finance)
food = Catagory(name='Food')
db.session.add(food)
health = Catagory(name='Health')
db.session.add(health)
history = Catagory(name='History')
db.session.add(history)
home = Catagory(name='Home')
db.session.add(home)
horror = Catagory(name='Horror')
db.session.add(horror)
language = Catagory(name='Language')
db.session.add(language)
music = Catagory(name='Music')
db.session.add(music)
nonfiction = Catagory(name='Non-Fiction')
db.session.add(nonfiction)
other = Catagory(name='Other')
db.session.add(other)
poetry = Catagory(name='Poetry')
db.session.add(poetry)
politics = Catagory(name='Politics')
db.session.add(politics)
reference = Catagory(name='Reference')
db.session.add(reference)
religion = Catagory(name='Religion')
db.session.add(religion)
romance = Catagory(name='Romance')
db.session.add(romance)
short = Catagory(name='Short Stories')
db.session.add(short)
sport = Catagory(name='Sport')
db.session.add(sport)
thriller = Catagory(name='Thriller')
db.session.add(thriller)
travel = Catagory(name='Travel')
db.session.add(travel)
true_crime = Catagory(name='True Crime')
db.session.add(true_crime)
db.session.commit()

# Create and add default catagory items (books)
animal_book = CatagoryItem(
    name='The Animal Book',
    author='Steve Jenkins',
    description="Our world is filled with extraordinary diversity, from amoebas to zebras, from tiny toadstools to giant oaks. The wonders of the natural world are on display in The Animal Book. This guide to life on our planet is packed full of information about creatures big and small. This tome is structured according to scientific classification, with straightforward explanations of more than 1,500 specimens, each stunningly photographed. A \"tree of life\" greets readers at the beginning of the book, charting the complex and interconnected relationships between species. Every plant and animal is presented in proportion, with in-depth spreads giving a sense of scale to each organism. Feature spreads that focus on a single specimen let children get up close and personal with the world's most fascinating animals, making The Animal Book perfect not only for homework help but to satisfy kids' curiosity about the wealth of living creatures that inhabit our planet.",
    picture='https://donalynmiller.files.wordpress.com/2013/12/animal-book.jpg',
    catagory_id=animal.id
)
db.session.add(animal_book)
art_book = CatagoryItem(
    name='Art of Coloring Star Wars: 100 Images to Inspire Creativity and Relaxation',
    author='Catherine Saunier-Talec, Anne Vallet',
    description="Relax, and let the creativity flow through you. Whether a skilled artist or an everyday dabbler of drawings and doodles, fans of all ages will enjoy these stunning pen-and-ink illustrations of beautiful landscapes, elaborate patterns, and memorable characters from the Star Wars universe. The lovely packaging includes a board cover with metallic foil stamping.",
    picture='http://ecx.images-amazon.com/images/I/515vhE9IDbL._SY344_BO1,204,203,200_.jpg',
    catagory_id=art.name
)
db.session.add(art_book)
autobiography_book = CatagoryItem(
    name='Autobiography Of Benjamin Franklin',
    author='Benjamin Franklin',
    description="Benjamin Franklin's writings represent a long career of literary, scientific, and political efforts over a lifetime which extended nearly the entire eighteenth century. Franklin's achievements range from inventing the lightning rod to publishing Poor Richard's Almanack to signing the Declaration of Independence. In his own lifetime he knew prominence not only in America but in Britain and France as well. This volume includes Franklin's reflections on such diverse questions as philosophy and religion, social status, electricity, American national characteristics, war, and the status of women. Nearly sixty years separate the earliest writings from the latest, an interval during which Franklin was continually balancing between the puritan values of his upbringing and the modern American world to which his career served as prologue. This edition provides a new text of the Autobiography, established with close reference to Franklin's original manuscript. It also includes a new transcription of the 1726 journal, and several pieces which have recently been identified as Franklin's own work.",
    picture='http://www.wpr.org/sites/default/files/images/shows/autobiographyben.jpg',
    catagory_id=autobiography.id
)
db.session.add(autobiography_book)
biography_book = CatagoryItem(
    name='The Second-Chance Dog',
    author='Jon Katz',
    description="From New York Times bestselling author Jon Katz comes a wise, uplifting, and poignant memoir of finding love against all odds, and the power of second chances for both people and dogs.",
    picture='http://mediad.publicbroadcasting.net/p/wamc/files/201311/jonkatz.jpg',
    catagory_id=biography.id
)
db.session.add(biography_book)
business_book = CatagoryItem(
    name='Think and Grow Rich',
    author='Napoleon Hill',
    description="Think and Grow Rich has been called the \"Granddaddy of All Motivational Literature.\" It was the first book to boldly ask, \"What makes a winner?\" The man who asked and listened for the answer, Napoleon Hill, is now counted in the top ranks of the world's winners himself.",
    picture='http://ecx.images-amazon.com/images/I/51DXwCR9fjL._SY344_BO1,204,203,200_.jpg',
    catagory_id=business.id
)
db.session.add(business_book)
children_book = CatagoryItem(
    name='Finding Winnie: The True Story of the World\'s Most Famous Bear',
    author='Lindsay Mattick, Sophie Blackall',
    description="In 1914, Harry Colebourn, a veterinarian on his way to tend horses in World War I, followed his heart and rescued a baby bear. He named her Winnie, after his hometown of Winnipeg, and he took the bear to war.",
    picture='http://ecx.images-amazon.com/images/I/61o-eULVflL._SX258_BO1,204,203,200_.jpg',
    catagory_id=children.id
)
db.session.add(children_book)
classics_book = CatagoryItem(
    name='The Catcher in the Rye',
    author='J. D. Salinger',
    description="Ever since it was first published in 1951, this novel has been the coming-of-age story against which all others are judged. Read and cherished by generations, the story of Holden Caulfield is truly one of America's literary treasures.",
    picture='https://upload.wikimedia.org/wikipedia/en/3/32/Rye_catcher.jpg',
    catagory_id=classics.id
)
db.session.add(classics_book)
comedy_book = CatagoryItem(
    name='Furiously Happy: A Funny Book About Horrible Things',
    author='Jenny Lawson',
    description="In Furiously Happy, #1 New York Times bestselling author Jenny Lawson explores her lifelong battle with mental illness. A hysterical, ridiculous book about crippling depression and anxiety? That sounds like a terrible idea.",
    picture='http://www.gannett-cdn.com/-mm-/a87a70a20b5d830e24245a232b72ac5f13822045/c=0-280-3000-4280&r=537&c=0-0-534-712/local/-/media/2015/10/02/DetroitFreePress/B9319106703Z.1_20151002161236_000_GR1C490UQ.1-0.jpg',
    catagory_id=comedy.id
)
db.session.add(comedy_book)
comic_book = CatagoryItem(
    name='The Walking Dead Compendium, Volume 1',
    author='Robert Kirkman',
    description="Introducing the first eight volumes of the fan-favorite, New York Times Best Seller series collected into one massive paperback collection! Collects The Walking Dead #1-48. This is the perfect collection for any fan of the Emmy Award-winning television series on AMC: over one thousand pages chronicling the beginning of Robert Kirkman's Eisner Award-winning continuing story of survival horror- from Rick Grimes' waking up alone in a hospital, to him and his family seeking solace on Hershel's farm, and the controversial introduction of Woodbury despot: The Governor. In a world ruled by the dead, we are finally forced to finally start living.",
    picture='http://img2.wikia.nocookie.net/__cb20121223185848/walkingdead/images/e/ee/Walking_dead_compendium_1.jpg',
    catagory_id=comic.id
)
db.session.add(comic_book)
computing_book = CatagoryItem(
    name='Head First C#',
    author='Jennifer Greene, Andrew Stellman',
    description="Head First C# is a complete learning experience for learning how to program with C#, XAML, the .NET Framework, and Visual Studio. Fun and highly visual, this introduction to C# is designed to keep you engaged and entertained from first page to last. Updated for Windows 8.1 and Visual Studio 2013, and includes projects for all previous versions of Windows (included in the book, no additional downloading or printing required).",
    picture='http://ecx.images-amazon.com/images/I/51IMT-N1RFL._SX431_BO1,204,203,200_.jpg',
    catagory_id=computing.id
)
db.session.add(computing_book)
culture_book = CatagoryItem(
    name='American Nations: A History of the Eleven Rival Regional Cultures of North America',
    author='Colin Woodard',
    description="An endlessly fascinating look at American regionalism and the eleven \"nations\" that continue to shape North America",
    picture='http://ecx.images-amazon.com/images/I/51I3Hux0TsL._SX324_BO1,204,203,200_.jpg',
    catagory_id=culture.id
)
db.session.add(culture_book)
comic_book = CatagoryItem(
    name='The Walking Dead Compendium, Volume 1',
    author='Robert Kirkman',
    description="Introducing the first eight volumes of the fan-favorite, New York Times Best Seller series collected into one massive paperback collection! Collects The Walking Dead #1-48. This is the perfect collection for any fan of the Emmy Award-winning television series on AMC: over one thousand pages chronicling the beginning of Robert Kirkman's Eisner Award-winning continuing story of survival horror- from Rick Grimes' waking up alone in a hospital, to him and his family seeking solace on Hershel's farm, and the controversial introduction of Woodbury despot: The Governor. In a world ruled by the dead, we are finally forced to finally start living.",
    picture='http://img2.wikia.nocookie.net/__cb20121223185848/walkingdead/images/e/ee/Walking_dead_compendium_1.jpg',
    catagory_id=comic.id
)
db.session.add(comic_book)
education_book = CatagoryItem(
    name='SAT Study Guide 2015: SAT Prep and Practice Questions',
    author='Sat Study Guide 2015 Team',
    description="Are you maximizing your SAT score? Traditional SAT study guides have followed the same format for decades. Written by independent, professional tutors to simulate the experience of private tutor sessions, the Accepted, Inc. SAT prep study guide is specifically designed for increasing ANY students score - regardless of their current scoring ability. With a page count at only 25\% the length of competitors study guides, this SAT Study Guide will increase your SAT score, while significantly decreasing your study time. Dont focus your attention relearning elementary school concepts. If you need to know it, its in our book. Our SAT Prep 2014 study guide does not contain filler or fluff , so you can work through the guide at a significantly faster pace than other SAT prep books. By allowing a student to focus ONLY on those concepts that will increase their score, study time is more effective; The student does not lose focus or get mentally fatigued. - 300 practice questions with worked-through solutions - Key test-taking tactics that reveal the tricks and secrets of the test - Simulated one-on-one tutor experience - Organized by concept with detailed explanations - College application tips included - SAT tips, tricks, and Test Secrets revealed - 25\% of the page count of most SAT study guides Get ready for the SAT in 2015 with Accepted, Inc.!",
    picture='http://ecx.images-amazon.com/images/I/510KcBvRHHL._SX385_BO1,204,203,200_.jpg',
    catagory_id=education.id
)
db.session.add(education_book)
fantasy_book = CatagoryItem(
    name='The Hobbit',
    author='J. R. R. Tolkien',
    description="Bilbo Baggins is a hobbit who enjoys a comfortable, unambitious life, rarely traveling any farther than his pantry or cellar. But his contentment is disturbed when the wizard Gandalf and a company of dwarves arrive on his doorstep one day to whisk him away on an adventure. They have launched a plot to raid the treasure hoard guarded by Smaug the Magnificent, a large and very dangerous dragon. Bilbo reluctantly joins their quest, unaware that on his journey to the Lonely Mountain he will encounter both a magic ring and a frightening creature known as Gollum.",
    picture='http://vignette1.wikia.nocookie.net/lotr/images/6/67/9780547928227_p0_v1_s260x420.jpg/revision/latest?cb=20130412192904',
    catagory_id=fantasy.id
)
db.session.add(fantasy_book)
fiction_book = CatagoryItem(
    name='To Kill a Mockingbird',
    author='Harper Lee',
    description="Harper Lee's Pulitzer Prize-winning masterwork of honor and injustice in the deep South-and the heroism of one man in the face of blind and violent hatred",
    picture='https://upload.wikimedia.org/wikipedia/en/7/79/To_Kill_a_Mockingbird.JPG',
    catagory_id=fiction.id
)
db.session.add(fiction_book)
finance_book = CatagoryItem(
    name='The Intelligent Investor',
    author='Benjamin Graham',
    description="The greatest investment advisor of the twentieth century, Benjamin Graham taught and inspired people worldwide. Graham's philosophy of \"value investing\" - which shields investors from substantial error and teaches them to develop long-term strategies - has made The Intelligent Investor the stock market bible ever since its original publication in 1949.",
    picture='http://ecx.images-amazon.com/images/I/51lKFg6ycnL._SY344_BO1,204,203,200_.jpg',
    catagory_id=finance.id
)
db.session.add(finance_book)
food_book = CatagoryItem(
    name='The Food Lab: Better Home Cooking Through Science',
    author='J. Kenji Lopez-Alt',
    description="A grand tour of the science of cooking explored through popular American dishes, illustrated in full color.Ever wondered how to pan-fry a steak with a charred crust and an interior that's perfectly medium-rare from edge to edge when you cut into it? How to make homemade mac 'n' cheese that is as satisfyingly gooey and velvety-smooth as the blue box stuff, but far tastier? How to roast a succulent, moist turkey (forget about brining!)-and use a foolproof method that works every time? As Serious Eats's culinary nerd-in-residence, J. Kenji Lopez-Alt has pondered all these questions and more. In The Food Lab, Kenji focuses on the science behind beloved American dishes, delving into the interactions between heat, energy, and molecules that create great food. Kenji shows that often, conventional methods don't work that well, and home cooks can achieve far better results using new-but simple-techniques. In hundreds of easy-to-make recipes with over 1,000 full-color images, you will find out how to make foolproof Hollandaise sauce in just two minutes, how to transform one simple tomato sauce into a half dozen dishes, how to make the crispiest, creamiest potato casserole ever conceived, and much more.",
    picture='http://ecx.images-amazon.com/images/I/41I6BS33vFL._SX258_BO1,204,203,200_.jpg',
    catagory_id=food.id
)
db.session.add(food_book)
health_book = CatagoryItem(
    name='Wheat Belly Total Health: The Ultimate Grain-Free Health and Weight-Loss Life Plan',
    author='William Davis',
    description="Wheat Belly Total Health answers the question, \"What's next in the battle against wheat?\" In his follow-up to the mega bestseller, Wheat Belly, Dr. Davis helps his readers take command over their life and health in the aftermath of wheat. There are many strategies that will help heal the damage caused by years of a wheat-filled diet. And many of these lessons have been learned in the years since the original Wheat Belly was released, lessons played out on the broad public stage of over one million readers, all participating in this grand adventure.",
    picture='http://ecx.images-amazon.com/images/I/41I6BS33vFL._SX258_BO1,204,203,200_.jpg',
    catagory_id=health.id
)
db.session.add(health_book)
history_book = CatagoryItem(
    name='New York Times Complete World War 2: All the Coverage from the Battlefields and the Home Front',
    author='The New York Times',
    description="The Times' complete coverage of World War II is now available for the first time in this unique package. Hundreds of the most riveting articles from the archives of the Times-including firsthand accounts of major events and little-known anecdotes-have been selected for inclusion in The New York Times: The Complete World War II. The book covers the biggest battles of the war, from the Battle of the Bulge to the Battle of Iwo Jima, as well as moving stories from the home front and profiles of noted leaders and heroes such as Winston Churchill and George Patton.",
    picture='http://ecx.images-amazon.com/images/I/51kcOfxg53L._SX376_BO1,204,203,200_.jpg',
    catagory_id=history.id
)
db.session.add(history_book)
home_book = CatagoryItem(
    name='Black & Decker The Book of Home How-To: The Complete Photo Guide to Home Repair & Improvement',
    author='Editors of Cool Springs Press',
    description="The editors at Cool Springs Press know a thing or two about DIY home improvement and maintenance; we've been writing about it for the past quarter-century, and we have more than a few bestsellers under our tool belts. Until now, there's been one thing missing: an ultimate, fully-loaded, ridiculously overpacked reference book for every home project you can dream of; the compilation of our longstanding expertise; the home how-to book to crush all others. The good news doesn't stop there; Black & Decker The Book of Home How-To is designed to reflect the way we search for information today. You won't find chapters or long, boring introductions or even a table of contents. This book is an A-to-Z encyclopedia with precise how-to instructions and clear photos packed onto every page. With an expanded index that is incredibly intuitive and a simple, alphabetical strategy for organizing the information, you won't spend precious time wading through stuff you don't need to know. Finding first-rate information on home care has never been easier, and all the most common tasks around your home are covered-including electrical, plumbing, flooring, walls, windows and doors, cabinetry, insulating, heating and cooling, roofing and siding, and just about any repair or remodeling project you can imagine.",
    picture='http://d.gr-assets.com/books/1381324820l/18467660.jpg',
    catagory_id=home.id
)
db.session.add(home_book)
horror_book = CatagoryItem(
    name='H.P. Lovecraft: Great Tales of Horror',
    author='H.P. Lovecraft',
    description="H.P. Lovecraft: Great Tales of Horror features twenty of horror master H.P. Lovecraft's classic stories, among them some of the greatest works of horror fiction ever written, including: \"The Rats in the Walls,\" \"Pickman's Model,\" \"The Colour out of Space,\" \"The Call of Cthulhu,\" \"The Dunwich Horror,\" \"The Shadow over Innsmouth,\" \"At the Mountains of Madness,\" \"The Shadow out of Time,\" and \"The Haunter of the Dark.\"",
    picture='http://d.gr-assets.com/books/1335214448l/13446612.jpg',
    catagory_id=horror.id
)
db.session.add(horror_book)
language_book = CatagoryItem(
    name='Language Files: Materials for an Introduction to Language and Linguistics, 11th Edition / Edition 11',
    author='Department of Linguistics',
    description="Since its inception, \"Language Files\" has become one of the most widely adopted, consulted, and authoritative introductory textbooks to linguistics ever written. The scope of the text makes it suitable for use in a wide range of courses, while its unique organization into student-friendly, self-contained sections allows for tremendous flexibility in course design. The eleventh edition has been revised, clarified, and updated in many places. This edition includes an all-new syntax chapter, new files on language and culture and on writing systems, restructured semantics files, and many new examples, exercises, and activities. Additional readings have been added to all chapters, and the number of cross-references among chapters has been increased. In addition, the accompanying \"Language Files\" webpage has links to online resources and websites related to language and linguistics that instructors and students may find interesting.",
    picture='http://ecx.images-amazon.com/images/I/51H7vdveIxL._SX355_BO1,204,203,200_.jpg',
    catagory_id=language.id
)
db.session.add(language_book)
music_book = CatagoryItem(
    name='Alfred\'s Basic Piano Course Lesson Book, Bk 1A: Book & CD',
    author='Willard A. Palmer, Amanda Vick Lethco',
    description="This easy step-by-step method emphasizes correct playing habits and note reading through interval recognition. Lesson Book Level 1A begins by teaching basic keyboard topography and fluent recognition of white key names in relation to black keys. It focuses on simple rhythms and prepares students for intervallic reading with entertaining songs that focus on \"same,\" \"stepping up\" and \"stepping down.\" It then introduces lines and space notes in treble and bass clefs, melodic and harmonic intervals of 2nds, 3rds, 4ths and 5ths, and graduates to reading on the grand staff. It also introduces the flat and sharp signs. This course is most effective when used under the direction of a piano teacher or experienced musician.",
    picture='http://ecx.images-amazon.com/images/I/51hE8EqeAwL._SY373_BO1,204,203,200_.jpg',
    catagory_id=music.id
)
db.session.add(music_book)
nonfiction_book = CatagoryItem(
    name='The Big Short: Inside the Doomsday Machine',
    author='Michael Lewis',
    description="Truth really is stranger than fiction. Who better than the author of the signature bestseller Liar's Poker to explain how the event we were told was impossible - the free fall of the American economy - finally occurred; how the things that we wanted, like ridiculously easy money and greatly expanded home ownership, were vehicles for that crash; and how shareholder demand for profit forced investment executives to eat the forbidden fruit of toxic derivatives.\" Michael Lewis's splendid cast of characters includes villains, a few heroes, and a lot of people who look very, very foolish: high government officials, including the watchdogs; heads of major investment banks (some overlap here with previous category); perhaps even the face in your mirror. In this trenchant, raucous, irresistible narrative, Lewis writes of the goats and of the few who saw what the emperor was wearing, and gives them, most memorably, what they deserve. He proves yet again that he is the finest and funniest chronicler of our times.",
    picture='http://ecx.images-amazon.com/images/I/51u30uvjFaL._SY344_BO1,204,203,200_.jpg',
    catagory_id=nonfiction.id
)
db.session.add(nonfiction_book)
other_book = CatagoryItem(
    name='The 7 Habits of Highly Effective People: Powerful Lessons in Personal Change',
    author='Stephen R. Covey',
    description="One of the most inspiring and impactful books ever written, The 7 Habits of Highly Effective People has captivated readers for 25 years. It has transformed the lives of Presidents and CEOs, educators and parents- in short, millions of people of all ages and occupations.",
    picture='https://upload.wikimedia.org/wikipedia/en/a/a2/The_7_Habits_of_Highly_Effective_People.jpg',
    catagory_id=other.id
)
db.session.add(other_book)
poetry_book = CatagoryItem(
    name='The Iliad: A New Translation by Caroline Alexander',
    author='Homer, Caroline Alexander',
    description="Composed around 730 B.C., Homer's Iliad recounts the events of a few momentous weeks in the protracted ten-year war between the invading Achaeans, or Greeks, and the Trojans in their besieged city of Ilion. From the explosive confrontation between Achilles, the greatest warrior at Troy, and Agamemnon, the inept leader of the Greeks, through to its tragic conclusion, The Iliad explores the abiding, blighting facts of war.",
    picture='http://ecx.images-amazon.com/images/I/41%2BJMrA9ZDL._SX332_BO1,204,203,200_.jpg',
    catagory_id=poetry.id
)
db.session.add(poetry_book)
politics_book = CatagoryItem(
    name='Things That Matter: Three Decades of Passions, Pastimes, and Politics',
    author='Charles Krauthammer',
    description="A brillant stylist known for an uncompromising honesty that challenges conventional wisdom at every turn, Krauthammer has for decades dazzled readers with his keen insight into politics and government. His weekly column is a must-read in Washington and across the country. Now, finally, the best of Krauthammer's intelligence, erudition and wit are collected in one volume.",
    picture='http://d.gr-assets.com/books/1375397727l/17345217.jpg',
    catagory_id=politics.id
)
db.session.add(politics_book)

reference_book = CatagoryItem(
    name='Merriam-Webster\'s Pocket Spanish-English Dictionary (Pocket Reference Library)',
    author='Merriam-Webster',
    description="A compact guide to essential Spanish and English vocabulary. Over 40,000 entries English pronunciations given in the International Phonetic Alphabet (IPA) Bidirectional: English to Spanish and Spanish to English",
    picture='http://ecx.images-amazon.com/images/I/51V9ZMZRSEL._SX307_BO1,204,203,200_.jpg',
    catagory_id=reference.id
)
db.session.add(reference_book)
religion_book = CatagoryItem(
    name='NIV Study Bible, Personal Size',
    author='Zondervan',
    description="Since its first release in 1985, the Gold Medallion Award-winning NIV Study Bible has become the treasured and trusted companion of over nine million Bible readers. The in-depth notes are coded to highlight notes of special interest in the areas of character study, archaeology, and personal application. Visually arresting section breaks help you find your bearing in the Bible. Full-color photos, maps, and illustrations make this study Bible accessible and friendly. Referred to daily by millions of pastors, students, church leaders, and other Bible readers around the world, the over-20,000 NIV Study Bible notes are the handiwork of the same translation team that produced this Bible's text. The very best evangelical scholarship that brought you today's most popular modern English Bible also contributed to the most celebrated and widely used study notes in existence. All of these features, and more, also make it perfect for homeschool use.",
    picture='https://www.booksofthebible.com/stock/p612d.jpg',
    catagory_id=religion.id
)
db.session.add(religion_book)
romance_book = CatagoryItem(
    name='The Choice',
    author='Nicholas Sparks',
    description="#1 New York Times bestseller Nicholas Sparks turns his unrivaled talents to a new tale about love found and lost, and the choices we hope we'll never have to make. Travis Parker has everything a man could want: a good job, loyal friends, even a waterfront home in small-town North Carolina. In full pursuit of the good life - boating, swimming, and regular barbecues with his good-natured buddies - he holds the vague conviction that a serious relationship with a woman would only cramp his style. That is, until Gabby Holland moves in next door. Spanning the eventful years of young love, marriage and family, THE CHOICE ultimately confronts us with the most heartwrenching question of all: how far would you go to keep the hope of love alive?",
    picture='http://d.gr-assets.com/books/1347368911l/2424355.jpg',
    catagory_id=romance.id
)
db.session.add(romance_book)
short_book = CatagoryItem(
    name='F. Scott Fitzgerald: Classic Works: Two Novels and Nineteen Short Stories',
    author='F. Scott Fitzgerald',
    description="No writer portrayed America's Roaring Twenties as vividly as F. Scott Fitzgerald. In his effervescent tales of elegant ingenues on the prowl for husbands, Ivy League heirs en route to futures of idle entitlement, and endless alcohol-fueled dance parties at ritzy country clubs, he limned a culture giddy with excess and as reckless as it was refined. Gifted with remarkable powers of observation and a witty way with words, Fitzgerald wrote stories that seem as fresh and modern today as they did when published nearly a century ago.",
    picture='http://33.media.tumblr.com/5410900d9c774829341506cae3f3058e/tumblr_inline_mtcotczMfd1qbtyk0.jpg',
    catagory_id=short.id
)
db.session.add(short_book)
sport_book = CatagoryItem(
    name='You Win in the Locker Room First: The 7 C\'s to Build a Winning Team in Business, Sports, and Life',
    author='Jon Gordon, Mike Smith',
    description="NFL head coach Mike Smith lead one of the most remarkable turnarounds in NFL history. In the season prior to his arrival in 2008, the Atlanta Falcons had a 4-12 record and the franchise had never before achieved back-to-back winning seasons. Under Smith's leadership, the Falcons earned an 11-5 record in his first season and would go on to become perennial playoff and Super Bowl contenders earning Smith AP Coach of year in 2008 and voted Coach of Year by his peers in 2008, 2010 and 2012.",
    picture='http://ecx.images-amazon.com/images/I/51bSlX-0vkL._SX320_BO1,204,203,200_.jpg',
    catagory_id=sport.id
)
db.session.add(sport_book)
thriller_book = CatagoryItem(
    name='Russian Hill',
    author='Ty Hutchinson',
    description="SFPD has no witnesses and no suspects, but FBI Agent Abby Kane believes a dead hiker found ten miles north of the city is the key to solving those crimes.",
    picture='http://ecx.images-amazon.com/images/I/51hD2qzc%2BhL._SX310_BO1,204,203,200_.jpg',
    catagory_id=thriller.id
)
db.session.add(thriller_book)
travel_book = CatagoryItem(
    name='Guide to the National Parks of the United States (5th Edition)',
    author='National Geographic',
    description="Featuring 80 all new maps and more than 350 photos, this guide is the most comprhensive, up-to-the-minute book of its kind on the market today. A perennial editions, it reflects National Geographic's century-long association with America's national parks system and its peerless reputation for travel expertise and cartographic excellence.",
    picture='http://ecx.images-amazon.com/images/I/41Mz2XaJMFL.jpg',
    catagory_id=travel.id
)
db.session.add(travel_book)
true_crime_book = CatagoryItem(
    name='Wiseguy',
    author='Nicholas Pileggi',
    description="Wiseguy: Life in a Mafia Family is a 1986 non-fiction book by crime reporter Nicholas Pileggi that chronicles the story of Mafia mobster-turned-informant Henry Hill.",
    picture='http://d.gr-assets.com/books/1328345463l/11758258.jpg',
    catagory_id=true_crime.id
)
db.session.add(true_crime_book)
db.session.commit()