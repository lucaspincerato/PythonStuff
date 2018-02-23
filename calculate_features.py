import requests

order_list = ['PORTALDASMALAS-e693b55bae6e4ed4a98e29fd1c21442d', 'EXCLUSIVASEX-4861bcee4b2346248a750a0446ce5e24', 'ATLANTAMATERIAIS-aa224987e6d949febde2dc7e3d4c9c17', 'CZ10COMBR-4b036a529f7c4b979a76a3d00753105e', 'EXCLUSIVASEX-307b775b3a074ec29fbe3fe096b23043', 'IPIRANGAGOLDEN-45c6a9f0475a4d069cf118cab28a6525', 'KDPNEUS-5bc3965c60c24b059b0f8dd5281d891b', 'KVRAXTECH-d200bb86f8814dfeac692e720207bcfe', 'MADRUGAOSUPL-3d5c111b5bf049d29ca4fbe8b09d699c', 'NAVE10-704139e0863b42c285d8182e5ff68b16', 'NAVE10-fea71c4789ab4cbc82f8c482b57619d3', 'PERKYINDECOM-2fe3e79ded744f109e71630c9049f3fd', 'PETELEGANTE-65b47f71976d468992891e5e154d402b', 'PORTALDASMALAS-bd73341a299f40c6ac6eaab3d5b0cf1a', 'PRESENTESMICKEY-124f8e05b8464d08bcf29851e25d5f47', 'PRESENTESMICKEY-3cee8d84e0184f32ac1279aef246938e', 'PRINCIPESSA-525e18bd1d7744e8aa70e57e2e3ce817', 'PRINCIPESSA-b4c76627272a4179802736e3afc1743d', 'PRINCIPESSA-b79d9fbddd454663940ab60e75c5c006', 'SOMOSCORUJA-857c7783c2cd4d7e82e975298c26f73e', 'UATTPRESENTES-12f70e26d83f431b87ef8f7bc1f07db6', 'UNCLEK-e9afa48d5ab04b9dbd7495b41cfce5e9', 'VINOMUNDIECOMMERCE-930e322412024966af228df4a02002eb', 'WORLDTENNIS-d369b5421a4642e2b193cf54d662d3f8', 'ZEEDOG-46fb42c3cd77404597c1d62ddd6a5ae3', 'ZEEDOG-6b5b954d1e334059816b7c019b593092', 'ZEEDOG-ead8a7f33cad4b21a224a64d79b08b7b', 'BAUDAELETRONICA-31b838edfd1e41beb40805eb5d38819c', 'BROFITWEAR-1093aecff0cd408782a4d9304fef75ee', 'CISSAMAGAZINE-d4c834fd3a1d48bd9bbe40f509d57b98', 'CZ10COMBR-05ae53cb6e2d4e4cab4da81139c1223a', 'CZ10COMBR-60a6b6f20f3f41a292420a10658daa56', 'CZ10COMBR-c9e0203b861b42c1863db9f068021dd6', 'DENTRODACAIXA-c5981014a6ff4d5681107c7f5376019c', 'FARMACIAMILIG-12453585059542e6a3cb1a6015cabac8', 'IMPORTADOSFAV-b9d9a1c497544713b2e796c9704ba98e', 'KVRAXTECH-3c7a864f617644f5b964d19f5990ce80', 'MAZESKATESHOP-3137b25ebcd14eae87cfbbc448dc6292', 'MAZESKATESHOP-6fcff810eb75464eba5b4a7f3ded370c', 'MAZESKATESHOP-eb6839f5e8254ce094ae8aa0c7a57eed', 'NAVE10-46c2d8348633468c8b3fb082098463c2', 'PETELEGANTE-1291355351234839848b4824e7231e88', 'PORTINHOLA-46e6ea30ab5f4cb9a863a811d528af43', 'PORTINHOLA-8054f97ce0ae45de8cda119acfc804e1', 'PRESENTESMICKEY-55c21371a46e450b984f954f9e0b5428', 'PRINCIPESSA-e0d19903732744f88cc40bfa1d71df3a', 'UIGAFAS-1eaf6d30a4f84a76baa4576ac85e82bc', 'UIGAFAS-27044a62dfab4b0f8d9ed453e091c759', 'UNCLEK-0ec25daf82094080bcdef2d2423e7e07', 'WORLDTENNIS-cc9ea26cc202487486e8a06ece483f83', 'ZEEDOG-71342592930d4b609cff18495821eb37', 'ARMADILLO-c22d4db34c464ea8b54c1723b9543069', 'ARMADILLO-d21dccf6afa948aab58fe8745073245b', 'ARTELASSE-2e890923d9374a50afce60ccc3e06ec5', 'BECODASPIPAS-3144c9ca67d84a6397bff683955f0f33', 'BRASILSELFSERV-92ce1d32bc2c4610a0745997d5b177d7', 'DAKOTACALCADOS-f919e040caa44f7d82cfd7adf933aed9', 'ECADEIRAS-bf37f8fad15745cca16a014336da1d0c', 'ECADEIRAS-c555658374054d599da5fa6e288c7ff3', 'EXCLUSIVASEX-c6308cf068b44fe5be0b65656d407f6d', 'EXCLUSIVASEX-f0d22f79eb09442cb9b11a0a9c628746', 'FALCONARMAS-9f49afd16e3d4eedac9584247b82a2d5', 'FARMACIAMILIG-a52fd517cd1b4044979dd07cdbe69c6e', 'FARMACIAMILIG-bc01da2a27904fbfadee79b80ed323f5', 'FARMADELIVERY-1a47edcc835d408c8864f1de026e35c2', 'FARMADELIVERY-2f97192fc4484b3eb58f8ae18d59ee8d', 'FARMADELIVERY-424a2abec90244c0890474dba920cf88', 'FARMADELIVERY-bae573dc97884af7908dcae384a53eb7', 'KDPNEUS-62bf2aa3f6244c518c0d4a0984c0cf9b', 'KDPNEUS-a621675c4c104b6f8ac0562509ee6741', 'MADRUGAOSUPL-0f0a2d755c14432682298125301e4721', 'MUNDODACARABINA-9e3f290264fd41d2872ffd0c939d5b34', 'ONOFREELETRO-0fd6e16d84de4d15911446745018a13d', 'ONOFREELETRO-10c25c8dddc8442e84ae60b8d3d0e88b', 'ONOFREELETRO-77eb9d529d4144109ef0a6d9c4623c46', 'PETELEGANTE-7e09a40c036a41d9b118537ff3c3be5b', 'PETELEGANTE-80dc40e721254546a103b052336edd17', 'PICHAU-f93d0c7bc4ea48e2a08da75707a31bd7', 'PORTINHOLA-4ee8db60f8524dd0bdde8d953ab5d1af', 'PRESENTESMICKEY-016846077cb445a0a2b0c993f427b5be', 'PRESENTESMICKEY-083c2231fc1844b0ac7d29d9f373964a', 'PRESENTESMICKEY-32f4e958cf3b4f7784b0ba03cd052908', 'PRESENTESMICKEY-73d9b68aabbe408fa8e2e231b9216a49', 'PRESENTESMICKEY-d7d9d1e3e858408dabd2513d1820f6e7', 'PRESENTESMICKEY-da5d4d8e393c46488bbc70f700ba79e2', 'PRODATA-19eb95a385c54c119783599a0fd7c7b4', 'SMSHOP-ffd8e3361a854051a569e748a97b7f26', 'STONEECLECTIC-7f768a1eeca34da49691d36df60bb5b8', 'TVZ-819e90d359d346db8e7ff792e32b1310', 'TVZ-a2f32da3d07642ccbb10dc6925e3756b', 'TVZ-edba10d71c7441988dd27b68b8c3ec5b', 'TVZ-ee12b9925cc4455992ebf22c2e51a458', 'VITRINEOUTLET-2747dc9bc365423bb09f50d49a200edc', 'ZEEDOG-069caaefa8434b369ec0f14a65ec8042', 'BRASILTAPETE-fc2f095dde754b539247047fddab3d54', 'BROFITWEAR-d7956fa1a95540c1b90332b3df58dee0', 'CISSAMAGAZINE-61e5cb272b7544f8979eba054ac7cd96', 'CISSAMAGAZINE-71cfd7b20c91449c87ed90c407ad6432', 'FALCONARMAS-c68a54e27998408cb3f8117b4dd9775f', 'FARMACIAMILIG-233dcdfc797c49308d6d1262d8fe9bd9', 'FARMADELIVERY-abbda91faa3d432ebfeafbe095a2e495', 'FARMADELIVERY-b286d184d9af4fb9bd2bfadb49e0ec57', 'IMPORTADOSFAV-5ca8c31087f8499bb220b5cf4aadec23', 'LIVEPASSGTW-4ed93a7d94ac4704aa564e168a398652', 'ONOFREELETRO-064d7b55359648b9a3b4faf4faf776a4', 'PANORAMAMOVEIS-2dc8b65ffb2b40f3853d8d31e7ad0be7', 'PEDIDOSJA-685d2f3fca624e8aa4ef4598484a6cd2', 'PEDIDOSJA-70f7fcd2ae1a430f8c4c6588524aecc4', 'PEDIDOSJA-7f85300b9cc948bd968d12099299c09f', 'PEDIDOSJA-a2a02fdcbcf14baba981a55525d0154f', 'PRESENTESMICKEY-0cd979866a7a4f6d88df1f02ace8afc4', 'PRESENTESMICKEY-48d2860205f1407bb1a7047fd4927df4', 'PRESENTESMICKEY-b3e6ae6719554c4abecf813955a4df13', 'PRESENTESMICKEY-b51c3dadce124b579cd349f32dffbc8e', 'PRESENTESMICKEY-d23f266a04c4439b99f3a48594b8aabc', 'SOMOSCORUJA-8057b8e6a65e4cc098c858d28626a725', 'TOPDRONE-671fdab346194332b20be88b05f6d3d3', 'TOPDRONE-e432b07663c5418481ac22f6894fb692', 'VINOMUNDIECOMMERCE-bc918b54c5e64c93a4b2bd79f8401deb', 'ZEEDOG-e80f9fe8a1ae42c8a36ffd2162ef3cdb', 'AGILEMED-4afaba48724442a685ca65d58d73f05b', 'ARTELASSE-23498e809829418d941935e7b895c920', 'CISSAMAGAZINE-19460b2d37bd47bf9ed7ceff21c45083', 'CZ10COMBR-7b19e0c308f145e19eab7ff45af64e48', 'DAKOTACALCADOS-72ba7984b6b94addbfd2305de274f28e', 'DALBERFASHION-c60335c2568b47de97e11da000799681', 'DASSIBOUTIQUE-93c51aee368748a7b25b782c5297d135', 'ECADEIRAS-9ccf4a4bfd384835884780fc15e60a3b', 'EXCLUSIVASEX-89a549691a5d47b4a37defbae6de5bfc', 'IPIRANGAPINW-0412c712531e4e2d9560d84ba6add69a', 'IPIRANGAPINW-34e094b4a6ad4063a7ef33f4ea8f2c2c', 'IPIRANGAPINW-61c1dc823878414ea13343171630ca2b', 'IPIRANGAPINW-c3889ccefe754cf1a84c0cf8fc42d802', 'IPIRANGAPINW-cf8731fd1b1b4a0e825af557314affa8', 'IPORTO-1624eafa00c84c488a70b1c9f2147096', 'MOVELMEUJEITO-6ad332e6268440c3b95478368adf95b2', 'MUNDODACARABINA-a9b5869de898425bbb2d79077b0d0ff1', 'PETELEGANTE-33a2ac1e45084913a98347d75ccefd18', 'PRESENTESMICKEY-51ffa4ee5bc14056b2be1a4d2ca52ff4', 'PRINCIPESSA-2975f94fa2304c84a9a12e3667635070', 'QUANTUM-8990b69448c14f95877612609f711b38', 'SHOPLOKO-e90ad9cbafdb49eea9ff2672926f6060', 'SOFAST-bc9be9c72a9840baa2bfed014662b73d', 'SOMOSCORUJA-7460599ede5440cb96e8b0e2f7a13fd2', 'ZEEDOG-99ff103a14614f469edbca04b7be0929', 'BARATOCOLETIVO-07c84af0a605499d86d965829b037060', 'BARATOCOLETIVO-125c29df247e45e6bb5d1c7836e6d84e', 'BARATOCOLETIVO-263234883b304b0f89aca87c1b95450e', 'BARATOCOLETIVO-4db7c71fead747509fdbf07dd4cda4eb', 'BARATOCOLETIVO-695d5d8485f0420482dca13460861a2c', 'BARATOCOLETIVO-945673a19376498ba42eef6f60588cd9', 'BARATOCOLETIVO-986b1ddb3bf94c42b4b0a38c9a7962c9', 'BARATOCOLETIVO-a81a4331b8cf4e6bbbdc7f1b20431938', 'BARATOCOLETIVO-c491c02909ed470dbb02356f64e9d5dd', 'CITEROL-6ff431ba0d84435f87b227f995400f00', 'DIPROTEC-60b30487f86a453097b004ea9575dae4', 'ECADEIRAS-4a12af435abf4bcc838516926fdd66e6', 'ECADEIRAS-6880462f01ea42babde6c69905bd8425', 'ESALFLORES-4ddc7cb8f12a477fab9790cb248bb964', 'ESALFLORES-d11fa8b3e17a4b3fb6f8c11edb788dbb', 'EXCLUSIVASEX-c10fd2bb00654e75a19ea00aa3bf956b', 'EXCLUSIVASEX-cbd4c57f339546d695f1ee186aa8e278', 'FANTASIASCAROL-70e3ad920cf24953a0572ea1bcd5ccc3', 'FARMADELIVERY-89ebcf788f004b3bbc006ce086ec3d3e', 'HOBBYPESCA-563b66f8f1b44d2ebd5d6744449f9374', 'IPIRANGAPINW-2216c78e36164cea81888356e464fbfa', 'LEVELNINE-8d4fae8b1d0443aaa29a6344fbf1615b', 'LIVEPASSGTW-0424ab48604e48d68a8835ce77656c14', 'LIVEPASSGTW-7f8c2f5d8096421d8f277be0d050dfe5', 'MAISAMIGAS-bf7857bee4054724a2625cd7ba94480e', 'MAZESKATESHOP-f4d5acb68b4845b2b44e6c19f1b143e6', 'MEC-9b66763981b245688ff5eb67ab39dc0f', 'MUNDODACARABINA-033f81b5b92b4d82b8828fa1748776de', 'PEDIDOSJA-5759ba8d0cea47b7866619fa731cee8c', 'PICHAU-0850d2013d7f483b84c07f73a32a0531', 'PICHAU-103cb00cfd6f4375b494475500dc2b6b', 'PICHAU-b7c58b340f6a41159bac0934c46ccab7', 'PICHAU-cd088892fbcc4489bae7963971087f00', 'PICHAU-d9b3cffd8d644406a717dd8051ea0f8e', 'PLATINUM4EVER-785bc8a5432143d2ad5b1fc06e8a1e87', 'PRESENTESMICKEY-2b5473970fe94446a42c04bbf0d52f52', 'SAINTSTUDIO-93a95d35182f422b8e83d2da3294bc4f', 'SEMIJOIAS-035d77d430694b5193bc465aae91285f', 'SOMOSCORUJA-3a890d4edf5a4854bbed59790e1e7260', 'TRIPTOMAX-508230df1a00436ea2a1779e35cf3579', 'TVZ-0b29bfcac2684371acd7a67b9d03ee3e', 'AGILEMED-cf4a621c9ac3415d85d4bb2e576e0c12', 'BARATOCOLETIVO-0257ddf739fe4056a67b56a89e18dffc', 'BARATOCOLETIVO-0a9b175ba55d49738029544bfbe2613d', 'BARATOCOLETIVO-19847fd3639c47948bd73024017de9f4', 'BARATOCOLETIVO-40512266d4a94ffebc1159d877b68719', 'BARATOCOLETIVO-567690f44dfc45a5a2e5c082b440e26d', 'BARATOCOLETIVO-5aac8dc22e074e9cb122e39c4b9b635a', 'BARATOCOLETIVO-64652c87bcbe43369f2aa4f0c424ea22', 'BARATOCOLETIVO-6f5492365b9e43eabf869555c507d2d1', 'BARATOCOLETIVO-b567cbf234664ef68fe295fea6f43aa7', 'DAKOTACALCADOS-66019891d4bf4b64aa7ae5c37db3aee9', 'DIGIPOPCONSULTA-46da29f49201499a84389007c7fba220', 'ECADEIRAS-d192897aaddb4ed6866bf42eed3560ec', 'ESSENCIABRASIL-8eb97b2bfad24183a9331b383d624168', 'EXCLUSIVASEX-4745fce8dbb84e4abca97d272f93ff93', 'EXCLUSIVASEX-8c8f1ec16d2842b8b99eab09d2570731', 'EXCLUSIVASEX-b24e800ca56247dab9ca2f0faef1a2a7', 'EXCLUSIVASEX-fcdcf7adea344aabacd6bd5c5305f543', 'FALCONARMAS-9e3805fb2cba44ea9572a1abf1fcc3bb', 'FARMADELIVERY-5e8d43e825f54ffc8c71e3df66e72f51', 'FARMADELIVERY-72bd3bd34abb4d35ab067c86d9b9ceae', 'FARMADELIVERY-a2412fe966cd4e05830e7f93749dd1b0', 'FARMADELIVERY-f24fce5a7c4f4cbe84f04cb8acbd6701', 'HOSTINGER-0fadd3c4ca0c4284a9faf0d0545d804c', 'HOSTINGER-3dfffe19e15f446197f66ff8898d653f', 'HOSTINGER-779cd9a670454a9dbec2f203ee5e7c2d', 'IMPORTADOSFAV-bbb3b11385cf460cbc648418a13a71b1', 'LIVEPASSGTW-573821af087b4c728cb438c0c306832b', 'LIVEPASSGTW-80e495506dbd4ab5bc5b40588247918a', 'LIVEPASSGTW-d64d7b5b44c74c50943e8081e17b275a', 'LIVEPASSGTW-e7f202dfb4944a9a9762f4b2b05dce45', 'LIVEPASSPSP-3e47ac27c13c48419050b0d7cabb6b7d', 'LMJOIASXTECH-2b3a8098a7db462db9ac8db2ce76cfec', 'METABOL-d5c31540ce7d40ae947265246b0bbe3f', 'MUNDODACARABINA-71c59c84f1fb499699edd6d8a32fdb2d', 'PEDIDOSJA-0029aa121f1a4d99adb9d69c434d9fe5', 'PEDIDOSJA-023d9bd614464776ba6bfdf7c25eb500', 'PEDIDOSJA-0c2865d7a02c4b438d1f2c1e2bd4ccea', 'PEDIDOSJA-0fc8774d22574ee7b03ec41581a53f74', 'PEDIDOSJA-1aefc563b61e44119c250aef4b4536e9', 'PEDIDOSJA-2fe9481d8bd34f0db112292546b0aebb', 'PEDIDOSJA-4ab88679af544ab8b61fd2ad2e9941f5', 'PEDIDOSJA-4b11954e8de64f958bdfe0c2a8445bd2', 'PEDIDOSJA-5629196d851e44149214d4328d8701c0', 'PEDIDOSJA-71fe666fb74445008a2f35d34e508cbe', 'PEDIDOSJA-764c64bb9c1e48c49ba1c78144ad3880', 'PEDIDOSJA-79f7a680de5f4c02bcfb9be95b348b0a', 'PEDIDOSJA-7a318e4217854208956e4cba0946c4b7', 'PEDIDOSJA-7ce51137843549feb52071172ad9c575', 'PEDIDOSJA-88ffc98444a94c048478bfbd8a3fc59e', 'PEDIDOSJA-a2522a5e4fce4416a2393c5e886d8056', 'PEDIDOSJA-cad5b305d6c048c5b5b228a8aae63ee8', 'PEDIDOSJA-d003a0bd8f0e436f9c4e98a50a8ff192', 'PEDIDOSJA-d10c16af683c4347bd7e13a26071415b', 'PEDIDOSJA-e1b1b86571674175ab4ab2d638fc720d', 'PEDIDOSJA-e3cf169ba97c4307a21e55a6b18b7d37', 'PEDIDOSJA-ef348e4d328d470d837776e683b802e4', 'PEDIDOSJA-fb6f37486f25456eb971705fb25e07a5', 'PEPILA-2fedefd4ec4d40b78517a5aa9f72dc41', 'PICHAU-d8dca34fcf704404bc71e4dfe6353852', 'PLATINUM4EVER-fc4d59e86da44304b47e35ce6ef70ff0', 'PRESENTESMICKEY-17e3dd5327a6435c8172f90171dac2f4', 'PRESENTESMICKEY-72762e9c30c64a53b838f5dea9c6f7d6', 'PRESENTESMICKEY-9a1437f59f9f4b5b99d78c2eecaf5aed', 'PRESENTESMICKEY-aa095cb2184a4535bfd7b13e23f3c702', 'PRINCIPESSA-34b1464416ad487a9ae0160079669808', 'SOMOSCORUJA-2b58a1aea60c4239b758d7039d5b85ac', 'SOMOSCORUJA-935f9545ba634e509efd8286d039c4cb', 'STONEECLECTIC-996468fe00c74f699ac6d0d889418915', 'STRARCONDICI-ce64276380e44062bba453408777ad04', 'TIOBOB-dce6417709c84391ad6f1e99c7f6d55c', 'VITRINEOUTLET-025d4c4e7be84798bf4ceae48625cbfc', 'VITRINEOUTLET-1cc655959e874a0da4b8eff8b0dc123a', 'VITRINEOUTLET-33a16f38a9ed4673868085d92d397fa6', 'VITRINEOUTLET-409fe09ff99c4398a85193b93dcb9798', 'VITRINEOUTLET-af82b9d9a4e749f4bb4456bee6a60a75', 'BARATOCOLETIVO-1633af50dd2f463e9ddab75720c8fa69', 'BARATOCOLETIVO-34a4b4717e0d486db5c19ce9801678da', 'BARATOCOLETIVO-63dd20cf8c0641498f746dec98ea3c31', 'BARATOCOLETIVO-8a3e61e8df9846018f628de9aa9acb68', 'BARATOCOLETIVO-ab69e949e13142fda2c62e7525a327f0', 'BARATOCOLETIVO-fc388eeb18174d1eaae17dcec544827c', 'BRASILCOWBOY-740c56c7c7aa4088beb8f83bc5fc70e1', 'CISSAMAGAZINE-12477adbccc2415b95bfbf2a0e39377e', 'CISSAMAGAZINE-858201653a994294bc881793376bfed2', 'CISSAMAGAZINE-9a5a19420dd64cbb851e50fe7d4de30d', 'CISSAMAGAZINE-9c920589ce974198bd6e762f7b0cab0b', 'CISSAMAGAZINE-af468f2ed8624ec4b5f0eecc425f950c', 'CISSAMAGAZINE-e733713e8c574f31900aeb520eda2d8c', 'CORPY-4ab0443e1fb24c9dad3238d2b7585eee', 'DIGIPOPCONSULTA-1f37abda2b664b6fab669d6f93ea3221', 'ECADEIRAS-a403a1f36d28446eb25d172185773232', 'ELGSCREEN-928ec1286de74d05a5ea16edabd7c612', 'EXCLUSIVASEX-23fdb444bbdb4da6afa18662b6bfaa71', 'EXCLUSIVASEX-d7ce487364d34b5cb2811f213602f3d9', 'FARMADELIVERY-3c0806be17b8445b80e2f4975f271406', 'FARMADELIVERY-acac0cf24e23449eafa02ab95e4ea9d0', 'FARMADELIVERY-d096d1fca83e4fe6a4173f6996570ad5', 'HAIRCAPS-d104881165a74983bc0e504b70904ae8', 'IMPORTADOSFAV-bbbfa7cbd90848deb41aa0420597d813', 'IPIRANGAPINW-2b14d306a39642388c74cba57532c2c4', 'IPIRANGAPINW-2bd75c2971b84efaa73aff948bb38fa8', 'KANGOOJUMPS-ec4e3e5a530a469ab3e0bf31d74cee44', 'LEVELNINE-b83cb5fcc39e4cfaa3a4652a6e69eea6', 'LIVEPASSGTW-1557c414ad1247a48ecfcbfd64e94c6d', 'LIVEPASSGTW-3917fca62a3d41fba0871051bf20b252', 'LIVEPASSGTW-54633d0f057746e6ade1734f4b232505', 'LIVEPASSGTW-69daf7a8b7e34502890c417f991e4d55', 'LIVEPASSGTW-daa9a7f33e994746a952c71e1c9d5301', 'LIVEPASSPSP-56e63e2dd4174efdbaa577bbeee74269', 'LIVEPASSPSP-88b362ac8f8b4f7bb438376265474394', 'MAISAMIGAS-d041a358be344b84abf5068756d11e83', 'METABOL-9726d76a6598427fbe6dc65f95e39d83', 'ONOFREELETRO-bfb5c243d6c74f9d825e83b2ce6bcd0e', 'PEDIDOSJA-1ded94baae594179b84e0e10e2bbecc6', 'PEDIDOSJA-23497c8bdc8f45e08f40f26a511b2d38', 'PEDIDOSJA-2900a9cac083408da5457cf70eea118d', 'PEDIDOSJA-4dd85ead910d458bb5f0c8b1027cfb53', 'PEDIDOSJA-7a0f6f60675c434b9a475eb0b95d58a4', 'PEDIDOSJA-8ad77d76404c43e38c48ebb2bb353c6f', 'PEDIDOSJA-9a125f08dc214469a27c22f60abff409', 'PEDIDOSJA-dc612a38a898458d830324e8ac1b3194', 'PEDIDOSJA-ec6a601496fb4a9d8d23714e5e63748b', 'PEDIDOSJA-ee50e965f34945598721c3b8f1592334', 'PERKYINDECOM-9a9e83c1bf024ffebe5f3879c08b82d7', 'PICHAU-0389a6ca037143b7a34f4890c2b5282a', 'PICHAU-12d6156e8bb44f9eb3eafa510e1e03f8', 'PICHAU-40922b9c52bf490e97ed4b8a683c2140', 'PICHAU-6a632806ac5c48d5b4ba7295b4d0258e', 'PURIFLORA-8ded49ebb340423aa5dcf567dbffa897', 'SOMOSCORUJA-5787843b4ff94c719e87c96746fd769c', 'TIOBOB-08296b14c085444eb35001f306b1e1c3', 'TIOBOB-1bc2640af7484a119bca5487e917785f', 'VITRINEOUTLET-49d8997947fd40cfa1a0f3dd7b516da3', 'VITRINEOUTLET-6f3f436367c247bf802ed321db791355', 'BARATOCOLETIVO-1752ae75330d43d0b56949807d10d5de', 'BARATOCOLETIVO-72184e8c0764454cacb206894ec022ae', 'CISSAMAGAZINE-091a1f83fe15443dbeb2beab8ac96883', 'CISSAMAGAZINE-4526b61ea5dd4fcf88970cf97ce35cae', 'CISSAMAGAZINE-5edd65c83df0448ca9bf34f9d8ca5f62', 'CISSAMAGAZINE-73e5cdd767cd40a8841cbd05ee1a16db', 'CISSAMAGAZINE-d09baf92e7c84b02b0aaead556f8a56f', 'FARMADELIVERY-3f3f6b4d527c45f8a78897004dbb2836', 'HAIRCAPS-c6262c614a5748ffacaa9d5197e830ae', 'HANDBOOK-869dea4dd1294488b14847191284adca', 'HOSTINGER-707500f695a14a818386bf7bb7f9b5d2', 'IMPORTADOSFAV-62d49b974c5848a8ae2458d09cdbb4d8', 'IPIRANGAMULTIP-07efcd54023e4ea0ba6a4a671e2ff0d9', 'IPIRANGAMULTIP-0b077ff28a3c4738bef727d9621be3a4', 'IPIRANGAMULTIP-0e4ba682b28e43abaaf39920c40dd34d', 'IPIRANGAMULTIP-18171b15834b4b6dbf0be57460c18493', 'IPIRANGAMULTIP-1c1bd7fad50d4aeb9036f376d50be1ab', 'IPIRANGAMULTIP-30471757779743e3abf082aba96a8786', 'IPIRANGAMULTIP-392610b58ab149c792045a3d079f9c56', 'IPIRANGAMULTIP-3e6e353189124104a639a85c671a4884', 'IPIRANGAMULTIP-47048c24049641ccb0df014ff1306194', 'IPIRANGAMULTIP-4d9552189fd34b9086d00f47b0de1f90', 'IPIRANGAMULTIP-601193686f3549e5a58981cee04e2902', 'IPIRANGAMULTIP-7241c18a579c485d93261ce32eb90749', 'IPIRANGAMULTIP-7283b46ff8a54215921ce36d4fbcd44d', 'IPIRANGAMULTIP-8fe358877dcc4d8aa25506dd48cf9c4c', 'IPIRANGAMULTIP-a25ae9310b3c49ac8c518e3776ab7a16', 'IPIRANGAMULTIP-bc31ee35fd324e099d1cfaf945e2bc3e', 'IPIRANGAMULTIP-ca9c225110394551a655c56849059044', 'IPIRANGAMULTIP-d1ec66cea61d4e5abe097788a15683e7', 'IPIRANGAMULTIP-d65e4a7b79364e7dbd78cd6ec56c9b9b', 'IPIRANGAMULTIP-d9af3874cacf4c02938c2a6c4e589b39', 'IPIRANGAMULTIP-da914a3bc5654c1fa10ae623ba171872', 'IPIRANGAMULTIP-dfd8d0ecc7254654bb5a97bff83e2d62', 'IPIRANGAMULTIP-e2fa928918ef4d20830eb41332e1e533', 'IPIRANGAMULTIP-e4c33121565344dabfaf56cc9f6783f6', 'IPIRANGAMULTIP-ed9ca405b1d0483b860c8bef73473317', 'IPIRANGAMULTIP-f3a1b61d13f048918764b0f490ad4c5c', 'IPIRANGAPINW-449ac0a3f23d4593af12bf555674e6d2', 'IPIRANGAPINW-796d4c0f6d01469793ead3c486f121c6', 'LEVELNINE-b0b4284085344562b5644b49b0a0a815', 'LIVEPASSGTW-17c7be7d88eb427e816dc21f790ca060', 'LIVEPASSGTW-418aeca502244f56a4c53a912bbe598a', 'LIVEPASSGTW-e3b8f06b89834027a078ad5d2569d888', 'ONOFREELETRO-535137a69e294ee1a1d67dc95645f39d', 'PEDIDOSJA-35f20143dc2f43cb92d1d60157594131', 'PEDIDOSJA-7441ba3b755a41138c972d3f93ec44b8', 'PICHAU-39e5c285463b4ea18c49a2ffa0abbc88', 'PICHAU-5eb38a0d29c5462b985b509625388265', 'PICHAU-8b22378f6bae40b1ba0070ed901ec82a', 'PICHAU-df5b9976d12d4e5fa302f56fc4e3a4bb', 'PLATINUM4EVER-843e658daf9a40b4af84980f0c15d876', 'SOMOSCORUJA-259af902081c4c59a74335bfbbfcee17', 'TIOBOB-b3558d09237d4638a56c29e352e5b74a', 'TRIPTOMAX-9856c6eb6a7d40cb842e17e50dbf1e1c', 'WEBLINK-d94db30e1fd745e486ca8021f0ccc427', 'BANNET-124779abacc347319a78ca29c6bf50de', 'BARATOCOLETIVO-c2978b51fffd4718a11b585dfb4fd3cd', 'BARATOCOLETIVO-c84027378f5b4fbdaf14c6979eaa7bd9', 'BARATOCOLETIVO-c8a48b671174412d8ffafe9d0cc5d933', 'BARATOCOLETIVO-d3842876869045699a6e9c395daffa68', 'CISSAMAGAZINE-ba19910dc8bb428b8d987a8d84c505e0', 'CORPY-625412579c354f79934ec4560f24d8f6', 'DIGIPOPCONSULTA-208f359377a648eaab5e87d6d0e3e3aa', 'FARMADELIVERY-4a416bf78016407ba43130540968c3d8', 'HOSTINGER-2f9bd9657afd4f9b9438a202a6c0072b', 'IPIRANGAMULTIP-044b925a910147b3bfc164a540af8fdc', 'IPIRANGAMULTIP-3707466d2dad42978353f861193eec78', 'IPIRANGAMULTIP-3ff9c8b88d884b2a80aab472fd8b5cb6', 'IPIRANGAMULTIP-41d21d2877cf4d1695431d4ab8afa482', 'IPIRANGAMULTIP-43a372fdb53344ea83d08603be25f0ec', 'IPIRANGAMULTIP-46f25c576ecc4e61a316ad757c87d907', 'IPIRANGAMULTIP-5c427305beec4b3e9158fa4174651fa0', 'IPIRANGAMULTIP-6382c5ded641484293f657bfd2cb0248', 'IPIRANGAMULTIP-67773d79b9ce42f697620018d8128092', 'IPIRANGAMULTIP-68b05df427c342889f57308970bb8e04', 'IPIRANGAMULTIP-8e0218c490f84b29a21d8bd4b3957a03', 'IPIRANGAMULTIP-908028c431da4e869e9e3572fa9911a1', 'IPIRANGAMULTIP-9f0d1bf285364b40b983c3b65b94f9b4', 'IPIRANGAMULTIP-a65fc25229f4404f966618c4cc2f5324', 'IPIRANGAMULTIP-b4cda3570331408dbbf85a85c9207c66', 'IPIRANGAMULTIP-d6360fbe8094485e917f1a21a6616b50', 'IPIRANGAMULTIP-e5a94f1b4d994eedaf0a98577790cffa', 'IPIRANGAMULTIP-e66ef7fe303b4ead941b05365745b89f', 'IPIRANGAMULTIP-eba7c2fc861041f9b0b63d6fb583ca0c', 'IPIRANGAPINW-5ee811d56c674be5954aea6a9c6a0a3c', 'IPIRANGAPINW-9b8c73475b5d4d699886f4b11bac63c1', 'LIVEPASSGTW-12c548c27b344a7ca5b37f61fcc93134', 'LIVEPASSGTW-524d5b9430604abda9a7193b8f845aeb', 'LIVEPASSGTW-5e52de0e4db040f89df0b3fd82421ec3', 'LIVEPASSGTW-6acac9441505484d82a54a9c7a5a4eb6', 'LIVEPASSGTW-86a9e0ead77b447c849782a6ac7147d9', 'LIVEPASSGTW-9386b48aa4e24387afc2e75172f7df8d', 'LIVEPASSGTW-ed5daded743b466ebc9b87db36e363d2', 'LIVEPASSGTW-ed741ed2fbcf41c9bb5e578d61b12181', 'MILIGRAMAOMNI-8af63298f82c4877822c4ad57d72b3e7', 'PEDIDOSJA-82c563e674e64db38f453e1d1b60d8b1', 'SOMOSCORUJA-38d15408433347a881245509b77a8252', 'SOMOSCORUJA-9289a862adc143368feabc8b744adfe6', 'STRARCONDICI-786390e1e1604358aaabbf8e39ee868b', 'BARATOCOLETIVO-0c4564bfaf284c0a8813598e7c1cf167', 'BARATOCOLETIVO-10d6f8f8085f4be3a91b01ec877d2b1d', 'BARATOCOLETIVO-14a10920381a48c1b73bbb2e661cde39', 'BARATOCOLETIVO-283b056cd0d64ada8835d3f015ce3df9', 'BARATOCOLETIVO-298f45dbb7f0412bbc755d52dd0a8f4f', 'BARATOCOLETIVO-42853961868f456da97afe116ab88b14', 'BARATOCOLETIVO-565aa656ba0d4fada47bd7bcaf257773', 'BARATOCOLETIVO-643e4166a319470a8f587efd0b33a9d1', 'BARATOCOLETIVO-7604f5ef8af345f2a8e01dda7a4b23ab', 'BARATOCOLETIVO-833268ca43924e959281f959c7ac6882', 'BARATOCOLETIVO-888baa5a398f4c66b2b4b9d14051c592', 'BARATOCOLETIVO-b7df29da4a27445498b38cee0f555205', 'BARATOCOLETIVO-e4cf11f38e074cd5a0bb422885edb1bb', 'CISSAMAGAZINE-645b178857b5451e90ac4c75d914df1b', 'CISSAMAGAZINE-a5c0e8c6193d45c7986f3d5c75606f3b', 'CORPY-306a68893565474283137d3df6e64368', 'CORPY-c8d29719e9474161a01500e9cc029daf', 'DAKOTACALCADOS-8919826e5fc048a2aa8a624581e8a69d', 'DIGIPOPCONSULTA-a66ff5c455cb4ec9af627578b9730a9d', 'DIGIPOPCONSULTA-f0f6f23e116747dc986fc08e4aded56f', 'HOSTINGER-f70b545f9175418ba8c7dd97cd8c7dc2', 'IPIRANGAGAUCHAO-ae4ef982514f48c6b3f97068dd53925f', 'IPIRANGAMULTIP-00c64f40f2f34e87ba5b054880e4f477', 'IPIRANGAMULTIP-0213db85ecd14ee8a5c7688e7fd81c32', 'IPIRANGAMULTIP-0421cabf26274a30baf53c36a6646fd2', 'IPIRANGAMULTIP-09393ef5f4ef4bee9999a41ab84ab868', 'IPIRANGAMULTIP-0aa9c8512d1b4a6fa274eb46ed4d2f46', 'IPIRANGAMULTIP-0e241a9977c041d7933584d3a8ebbc51', 'IPIRANGAMULTIP-11063829c470496ea8dee8466fa5cca0', 'IPIRANGAMULTIP-11dd45f6e14b4906985c3b8a32446af2', 'IPIRANGAMULTIP-18c07e23a0aa4b3bbd8d1288e2a385e4', 'IPIRANGAMULTIP-1d51cbfb8c214dfebeb5ed96253de38c', 'IPIRANGAMULTIP-20a0692e221f4171b89bcd4e41d13733', 'IPIRANGAMULTIP-2433f364037d4ecf91b14c25bc6edbea', 'IPIRANGAMULTIP-2cdd6790ed274af48647f22a10b05001', 'IPIRANGAMULTIP-2d4a78b28288484dbab6b3c81e967702', 'IPIRANGAMULTIP-2f67a466d1eb4e26b7764a1684304199', 'IPIRANGAMULTIP-2fb7d0a0880c4a3faa56d62896b7ff4e', 'IPIRANGAMULTIP-35cd44ea63294fe1a7af9a82b06fb902', 'IPIRANGAMULTIP-3b1230881c7241ff9864f2afc61cb3ae', 'IPIRANGAMULTIP-3b290b8285c948e08cbf951743cc4832', 'IPIRANGAMULTIP-3dd992615d9b4f6585b6e9d639203659', 'IPIRANGAMULTIP-422b54ca4ec44476be6b3ebedb3a03d7', 'IPIRANGAMULTIP-4625c7df9b084bf08e47259cd9660756', 'IPIRANGAMULTIP-47338290599e443390f1a70f3b9d2a06', 'IPIRANGAMULTIP-4a60a72076234a42b0f64943f97f1dc4', 'IPIRANGAMULTIP-4cece56d1fe84533b2dbd67dbf689266', 'IPIRANGAMULTIP-4e7e8339abcd4dd2b0d98f54bde32bae', 'IPIRANGAMULTIP-4ecd6e3e3583487cb4112e1ed847da41', 'IPIRANGAMULTIP-500ca8f9cae5401280d5c0ee73d6b091', 'IPIRANGAMULTIP-502efdd1e05745a78de815773a4c7aaf', 'IPIRANGAMULTIP-51bd9c72567f491cbf5ec383e2fb361b', 'IPIRANGAMULTIP-574ec6b33d4940a6bd8999a83d4202b3', 'IPIRANGAMULTIP-5791f82baae24339833cb7fc066232f4', 'IPIRANGAMULTIP-5915e80fdb814f0dbd0c975e5e096810', 'IPIRANGAMULTIP-5a881cb92e164a4dac24d8a8576afa4f', 'IPIRANGAMULTIP-632bda1516cc4c6090159ece72cf0ee5', 'IPIRANGAMULTIP-6524b2e7fbd649acba74102279da8af5', 'IPIRANGAMULTIP-6f223154406040a4bb23ffa93e8c255e', 'IPIRANGAMULTIP-7190b436b4954a86b333430fdf5e44b8', 'IPIRANGAMULTIP-740317670a1b4edbacee1ec649fd79de', 'IPIRANGAMULTIP-74414fdd0d4c425284408792b6d2b825', 'IPIRANGAMULTIP-7ac334c3c2f443f58f7bcd9510cc692b', 'IPIRANGAMULTIP-7cff033c69124d7b9dd2b204ddc4a7f4', 'IPIRANGAMULTIP-7d7c49941abd4932a25a036c82781499', 'IPIRANGAMULTIP-7d85fdfe44394f42a370eaf1ef523474', 'IPIRANGAMULTIP-7eea84d4a67b4cbe83d5f9d8e6f41915', 'IPIRANGAMULTIP-82d5af8225b6470984daad251864ba16', 'IPIRANGAMULTIP-845b5e479def4ef2abfcf98c5f0fd66b', 'IPIRANGAMULTIP-8db059ca451440429339d2ba34c4617c', 'IPIRANGAMULTIP-9300208445ed491a8589505d4e95b2c1', 'IPIRANGAMULTIP-93a5a0b431b1467aa4487dc94800657c', 'IPIRANGAMULTIP-96159870f88d41a6a0c0e93310ca77a8', 'IPIRANGAMULTIP-a0924ad424c94d6b96798a6f83ac0819', 'IPIRANGAMULTIP-a659570b95da46b0bf5fb977ae496617', 'IPIRANGAMULTIP-ac389b8c7c63451c8fd6fb61748dda3d', 'IPIRANGAMULTIP-b2072552b84a45889119545e7810291f', 'IPIRANGAMULTIP-b3a0b26422d048148efeb898b34b5d9c', 'IPIRANGAMULTIP-b5d87825aa624ba98d3192f42188bae4', 'IPIRANGAMULTIP-b93b22a9b3ff488c82c852acbcbfe603', 'IPIRANGAMULTIP-bc8696cc5f1b4f29b314a5e7db484ebd', 'IPIRANGAMULTIP-c0a3f8e52fee4790a62a12e4fec08fc5', 'IPIRANGAMULTIP-c9dbd0268f7a49daaf62224453e8dc6e', 'IPIRANGAMULTIP-cdbcddc3732a4b628826ae5f0d49409f', 'IPIRANGAMULTIP-da973e1a5624487ca84098436cd5e5b1', 'IPIRANGAMULTIP-dbd74df71eb14674a4cf02474b1a1814', 'IPIRANGAMULTIP-dc3be7e517294224b0effb79b04758f9', 'IPIRANGAMULTIP-dc9ee23069f14d53b98b7f869fff5bc3', 'IPIRANGAMULTIP-df0a0dc931784ef084a1bd0c8e5cd1f2', 'IPIRANGAMULTIP-e31e26cb3ae8427ca8a4497f6affa157', 'IPIRANGAMULTIP-e45b097462354f3a81eb8cabc58120b9', 'IPIRANGAMULTIP-e78ac2eac775441591c8d9311a7b5907', 'IPIRANGAMULTIP-ec1d09157a344bc59b12b634dc8c6930', 'IPIRANGAMULTIP-ee6ffcb799994a53abb78f0b25023cf4', 'IPIRANGAMULTIP-f4d40549195c4b659bb590905e9acd46', 'IPIRANGAMULTIP-f5d5863f2e8c4b7485118a6f304124b7', 'IPIRANGAMULTIP-f620efdc87f34c51bd87d5a4d38a88c9', 'IPIRANGAMULTIP-fd3ad20e8b624396aa1ef1a24c0809e2', 'IPIRANGAMULTIP-ffd60978ab164f7aa4771e61e021ff1b', 'IPIRANGAPINW-ce092e32130c4b69ba62b37eeb12e464', 'IPONTOQUATRO-2353689f5d654da4813d9ea1160498cf', 'IPORTO-400221a2fc564534ae135d322db42927', 'LEVELNINE-24c929ba6b3e428ab0e663602125209f', 'LEVELNINE-951dd7e4635444ecad91683663e66627', 'LEVELNINE-f60358da386c41f9a3dcc6a55ed924fd', 'LIVEPASSGTW-1337ed1de59b4d99ba7d68e38a75157e', 'LIVEPASSGTW-176dfbe26fe546d1833072a674501fa0', 'LIVEPASSGTW-34ca7876b5d84eda90a2bc057627fb6d', 'LIVEPASSGTW-3c8461ba2205483b9dd546ae9cc1c12a', 'LIVEPASSGTW-462ca7bbfa0e4e1783c629fea1552a3b', 'LIVEPASSGTW-70ff9b70563346d9999baaa1492dbc48', 'LIVEPASSGTW-75eed2e9a6464a39988b11283f6ac959', 'LIVEPASSGTW-75f84034cfb44767a9aa1e3a840ab183', 'LIVEPASSGTW-78ffc2f31632475ba2b25c3d884b4f18', 'LIVEPASSGTW-7c755764f79d4ee7b9089eea71c35707', 'LIVEPASSGTW-83ac141f5b3f48a9858562b7ffbc76cb', 'LIVEPASSGTW-848ac07623e449348e7cc9df07e88f88', 'LIVEPASSGTW-866d8a7dabb245cda47efd0e95f53a47', 'LIVEPASSGTW-b45001ebba5f4a90ae3b11a0e0d01cff', 'LIVEPASSGTW-b4e9947231da44cfb6ec7eef9d93ef6f', 'LIVEPASSGTW-c15c3c1e7b5447f0b4f50c46d1a596d0', 'LIVEPASSGTW-ca8cf06c26f3461faa658f171c0ecc13', 'LIVEPASSGTW-d1498b039aee4847b265b3e935c00a56', 'LIVEPASSPSP-5b0cac5ad24043fd92ce03326d69773d', 'MILIGRAMAOMNI-fffcc6c911cf4471a49f10cd6c527770', 'PEDIDOSJA-3c6055de9d074f4682d00453eb177343', 'PEDIDOSJA-40bc86b996104028aedb51adb41ba5cd', 'PEDIDOSJA-4bad1c86875e4b9b86940e3f0156bcdc', 'PEDIDOSJA-4df2b5b05fe34dce9922608770a6bb63', 'PEDIDOSJA-9179d5c9b8af4099ac3a67d7ded67839', 'PICHAU-0c0bc7f40f17498c9bc4a9fc4b7bd543', 'PICHAU-41b83571419b471381cadaa4e03b925f', 'PICHAU-87193e2f81ab499ab4e97e5b656617e0', 'PICHAU-8a4d922b72e14adf8505ab24531a12fd', 'PICHAU-a5e695db0bbd47b8acae0657cc5f7210', 'PICHAU-edce4af4ada147cfb572c6eaaf406aa4', 'PMULOJA-538017ca1c74411ba29afb25945104d1', 'PRESENTESMICKEY-882fe4bfee514abab851cb88d0454f08', 'PRINCIPESSA-ab79b4d4a58e4989b4a038280871f150', 'SAGESCOSMETICOS-b99aacb9f8d3439994bacd161b65fee4', 'TRIPTOMAX-01e4b6705da146459c622a0220afc9b5', 'VITRINEOUTLET-710da291266e45219cd9cf781a8a30b9']


responseList = list()

for order in order_list:
    response = requests.get('http://featureservice-alb-public-702088323.us-east-1.elb.amazonaws.com/features/order/{}'.format(order)).content
    responseList.append(response)
    print '({}/{}) Acabei a order {}'.format(order_list.index(order), len(order_list), order)
    # print response

print responseList, '\n\n'

with open('/home/pincerato/code/data/features_from_timeout_orders.csv', 'wb') as file:
    for line in responseList:
        file.write(line)
        file.write('\n')

print 'THE END!'