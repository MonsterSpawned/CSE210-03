# Authors: Bryan Hunter and Aitana (Invitado)

class ParachutistStages():
        
    # Get the current stage of the parachutist string/print:
    def get_stage(self, stage):
        if stage in [1, 0, "first"]:
            return str(
                "\n{}" +
                " _____\n" +
                "/_____\ \n" +
                "\     / \n" +
                " \   / \n" +
                "   0 \n" +
                "  /|\ \n" +
                "  / \ \n" +
                "^^^^^^^\n" +
                "{}")
        if stage == 2:
            return str(
                "\n{}" +
                "/_____\ \n" +
                "\     / \n" +
                " \   / \n" +
                "   0 \n" +
                "  /|\ \n" +
                "  / \ \n" +
                "^^^^^^^\n" +
                "{}")
        if stage == 3:
            return str(
                "\n{}" +
                "\     / \n" +
                " \   / \n" +
                "   0 \n" +
                "  /|\ \n" +
                "  / \ \n" +
                "^^^^^^^\n" +
                "{}")
        if stage == 4:
            return str(
                "\n{}" +
                " \   / \n" +
                "   0 \n" +
                "  /|\ \n" +
                "  / \ \n" +
                "^^^^^^^\n")
        if stage == 5:
            return str(
                "\n{}" +
                "   0 \n" +
                "  /|\ \n" +
                "  / \ \n" +
                "^^^^^^^\n" +
                "{}")
        if stage in [6, "final", "last"]:
            return str(
                "\n{}" +
                "   X \n" +
                "  /|\ \n" +
                "  / \ \n" +
                "^^^^^^^\n" +
                "{}")
        else:
            print("Something went terribly wrong.\nPlease contact the developers of this program and give them the following error code:\n\n'PARACHUTIST_STAGE_VALUE_NOT_SET'")
