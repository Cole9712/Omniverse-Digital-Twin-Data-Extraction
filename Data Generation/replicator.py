import omni.replicator.core as rep
import random

with rep.new_layer():
    # Define paths for the character, the props, the environment and the surface where the assets will be scattered in.
    # Animals with animations
    COW_ATTACK = 'omniverse://localhost/Projects/Project assets/animated animals/cow-jump.usd'
    COW_ANGRY = 'omniverse://localhost/Projects/Project assets/animated animals/cow-angry2.usd'
    COW_EAT = 'omniverse://localhost/Projects/Project assets/animated animals/cow-drink.usd'
    COW_RUN = 'omniverse://localhost/Projects/Project assets/animated animals/cow-run.usd'
    COW_WALK = 'omniverse://localhost/Projects/Project assets/animated animals/cow-walk.usd'
    GOAT_EAT = 'omniverse://localhost/Projects/Project assets/animated animals/goat-eat.usd'
    GOAT_WALK = 'omniverse://localhost/Projects/Project assets/animated animals/goat-walk.usd'
    PIG_COMBO = 'omniverse://localhost/Projects/Project assets/animated animals/pig-comboAttack.usd'
    PIG_WALK = 'omniverse://localhost/Projects/Project assets/animated animals/pig-walk.usd'
    SHEEP_EAT = 'omniverse://localhost/Projects/Project assets/animated animals/sheep-eat.usd'
    SHEEP_WALK = 'omniverse://localhost/Projects/Project assets/animated animals/sheep-walk.usd'
    CHICKEN_EAT = 'omniverse://localhost/Projects/Project assets/animated animals/chicken-eat.usd'
    CHICKEN_LAY = 'omniverse://localhost/Projects/Project assets/animated animals/chicken-lay.usd'
    CHICKEN_RUN = 'omniverse://localhost/Projects/Project assets/animated animals/chicken-run.usd'
    CHICKEN_WALK = 'omniverse://localhost/Projects/Project assets/animated animals/chicken-walk.usd'


    # Static Animals
    COW0 = 'omniverse://localhost/Projects/Project assets/cow/Props/MeshCowBlack.usd'
    COW1 = 'omniverse://localhost/Library/Animals/Cow/Props/SK_Cow.usd'
    CHICKEN = 'omniverse://localhost/Library/Animals/Chicken/Props/SK_Chicken.usd'
    GOAT = 'omniverse://localhost/Library/Animals/Goat/Props/SK_Goat.usd'
    PIG = 'omniverse://localhost/Library/Animals/Pig/Props/SK_Pig.usd'
    SHEEP = 'omniverse://localhost/Library/Animals/Sheep/Props/SK_Sheep.usd'

    # Animation lists
    cow1 = [COW_ANGRY, COW_ATTACK, COW_RUN]
    cow2 = [COW_EAT, COW_WALK]
    chicken1 = [CHICKEN_LAY, CHICKEN_WALK]
    chicken2 = [CHICKEN_EAT, CHICKEN_RUN]
    goat = [GOAT_EAT, GOAT_WALK]
    pig = [PIG_COMBO, PIG_WALK, PIG]
    sheep = [SHEEP_EAT, SHEEP_WALK]

    # Environment assets
    PROPS = 'omniverse://localhost/NVIDIA/Assets/Vegetation/Shrub'

    camera_look_at = [(0,0,1300), (1800,0,1300), (580,0,-550), (3000,0,-1500)]
    cameraRangesX = [(-100, 400, 3400), (3600, 400, -2500), (-150, 300, -400)]
    cameraRangesY = [(3300, 800, 4000), (5500, 1500, 3334), (-900, 700, 3800)]
    animalRangesX = [(300, 0, -100), (2460, 0, 1900), (1050, 0, -1550), (1050, 0, -1550)]
    animalRangesY = [(450, 0, 2880), (2937, 0, 2880), (2370, 0, 2515), (2937, 0, 987)]

    def createAnimal(spceies, name, listOfPaths):
        animal = rep.create.from_usd(random.choice(listOfPaths), semantics=[('species', spceies), ('name', name)], count=1)
        with animal:
            choice = random.randint(0, len(animalRangesX)-1)
            rep.modify.pose(
                position=rep.distribution.uniform(animalRangesX[choice], animalRangesY[choice]),
                rotation=rep.distribution.uniform((-90,-180, 0), (-90, 180, 0)),
            )

    def dome_lights():
        lights = rep.create.light(
                light_type="Dome",
                rotation= rep.distribution.uniform((220,-180, 0), (270, 180, 0)),
                texture=rep.distribution.choice([
                    'omniverse://localhost/NVIDIA/Assets/Skies/Night/moonlit_golf_4k.hdr',
                    'omniverse://localhost/NVIDIA/Assets/Skies/Clear/noon_grass_4k.hdr',
                    'omniverse://localhost/NVIDIA/Assets/Skies/2022_1/Skies/Clear/lakeside.hdr'
                    ])
                )
        return lights.node
    
    def env_props(size=40):
        instances = rep.randomizer.instantiate(rep.utils.get_usd_files(PROPS), size=size, mode='point_instance')
        with instances:
            rep.modify.pose(
                position=rep.distribution.uniform((630, 0, -1800), (3300, 0, 2900)),
                rotation=rep.distribution.uniform((-90,-180, 0), (-90, 180, 0)),
            )
        return instances.node

    # Register randomization
    rep.randomizer.register(dome_lights)
    rep.randomizer.register(env_props)


    # Setup the static elements
    # env = rep.create.from_usd(ENVS)
    # surface = rep.create.from_usd(GROUND)

    # Setup camera and attach it to render product
    cameraOut1 = rep.create.camera(
        focus_distance=2500,
        f_stop=0.5
    )
    cameraOut2 = rep.create.camera(
        focus_distance=800,
        f_stop=0.5
    )
    # render_product = rep.create.render_product(cameraOut1, resolution=(1600, 900))
    render_product = rep.create.render_product(cameraOut1, resolution=(1024, 768))
    # render_product2 = rep.create.render_product(cameraOut2, resolution=(1600, 900))


    # Initialize and attach writer
    writer = rep.WriterRegistry.get("BasicWriter")
    writer.initialize(output_dir="J:\CMPT 732 Project\CMPT 732 Dataset", rgb=True, bounding_box_2d_loose = True, semantic_types=['species', 'name'])
    writer.attach([render_product])

    with rep.trigger.on_time(num=25, interval=1):
        # rep.randomizer.cow0()
        rep.randomizer.dome_lights()
        rep.randomizer.env_props(30)

        createAnimal('Cow', 'Sam', cow1)
        createAnimal('Cow', 'Lucy', cow2)
        createAnimal('Chicken', 'Ross', chicken1)
        createAnimal('Chicken', 'Mary', chicken2)
        createAnimal('Sheep', 'Elon', sheep)
        createAnimal('Goat', 'Alex', goat)
        createAnimal('Pig', 'Max', pig)
        choice = random.randint(0, len(cameraRangesX)-1)
        with cameraOut1:
            rep.modify.pose(position=rep.distribution.uniform(cameraRangesX[choice], cameraRangesY[choice]), 
                look_at=(1625, 0, 100)) 

        # with cameraOut2:
        #     rep.modify.pose(position=rep.distribution.uniform((-350, 300, -750), (550, 600, -570)), 
        #         look_at=(105, 0, -1700)) 
