import java.util.Scanner;
import java.util.Random;
import java.io.IOException;
import java.math.BigInteger;
 
public class RSA {
	private BigInteger p;
	private BigInteger q;
	private BigInteger N;
	private BigInteger phi;
	private BigInteger e;
	private BigInteger d;
	private int		   bitlength = 1024;
	private Random	   r;

	public RSA() {
		r = new Random();
		p = BigInteger.probablePrime(bitlength, r);
		q = BigInteger.probablePrime(bitlength, r);
		N = p.multiply(q);
		phi = p.subtract(BigInteger.ONE).multiply(q.subtract(BigInteger.ONE));
		e = BigInteger.probablePrime(bitlength / 2, r);
		while (phi.gcd(e).compareTo(BigInteger.ONE) > 0 && e.compareTo(phi) < 0)
			e.add(BigInteger.ONE);
		d = e.modInverse(phi);
	}

	public static void main(String[] args) throws IOException {
		RSA rsa = new RSA();
		Scanner in = new Scanner(System.in);

		System.out.println("Enter the plain text:");
		String teststring = in.nextLine();
		// String teststring = args[0];

		System.out.println("Encrypting String: " + teststring);
		System.out.println("String in Bytes: " + bytesToString(teststring.getBytes()));
		// encrypt
		byte[] encrypted = rsa.encrypt(teststring.getBytes());
		// decrypt
		byte[] decrypted = rsa.decrypt(encrypted);
		System.out.println("Decrypting Bytes: " + bytesToString(decrypted));
		System.out.println("Decrypted String: " + new String(decrypted));
	}

	private static String bytesToString(byte[] encrypted) {
		String temp = "";
		for (byte b : encrypted) 
			temp += Byte.toString(b);
		return temp;
	}

	// Encrypt message
	public byte[] encrypt(byte[] message) {
		return (new BigInteger(message)).modPow(e, N).toByteArray();
	}

	// Decrypt message
	public byte[] decrypt(byte[] message) {
		return (new BigInteger(message)).modPow(d, N).toByteArray();
	}
}