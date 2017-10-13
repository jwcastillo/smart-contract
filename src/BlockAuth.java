import org.neo.smartcontract.framework.SmartContract;
import org.neo.smartcontract.framework.services.neo.Storage;

public class BlockAuth extends SmartContract {

    public static void Main(String challenge) {
        Storage.put(
                Storage.currentContext(),
                "challenge",
                challenge
        );
    }

}