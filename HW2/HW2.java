import javax.crypto.Cipher;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.BadPaddingException;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;
import java.util.Scanner;

public class HW2 {

  static byte[] generateKey() {
    byte[] key = new byte[16];
    for (int i = 0; i < key.length; i++) {
      key[i] = (byte) (i + 1);
    }
    return key;
  }

  static byte[] shuffleBlocks(byte[] inputArray, int blockSize) {
    int blockCount = inputArray.length / blockSize;
    byte[][] blocks = new byte[blockCount][blockSize];

    for (int i = 0; i < blockCount; i++) {
      System.arraycopy(inputArray, i * blockSize, blocks[i], 0, blockSize);
    }

    byte[][] shuffledBlocks = new byte[blockCount][];
    shuffledBlocks[0] = blocks[2];
    shuffledBlocks[1] = blocks[1];
    shuffledBlocks[2] = blocks[0];

    byte[] shuffledArray = new byte[inputArray.length];
    for (int i = 0; i < shuffledBlocks.length; i++) {
      System.arraycopy(shuffledBlocks[i], 0, shuffledArray, i * blockSize, blockSize);
    }

    return shuffledArray;
  }

  static void P1() throws Exception {
    byte[] cipherBMP = Files.readAllBytes(Paths.get("cipher1.bmp"));
    byte[] key = new byte[16];
    for (int i = 0; i < 16; i++) {
      key[i] = (byte) (i + 1);
    }
    byte[] iv = new byte[16];
    SecretKeySpec keySpec = new SecretKeySpec(key, "AES");
    IvParameterSpec ivSpec = new IvParameterSpec(iv);
    Cipher cipher = Cipher.getInstance("AES/CBC/ISO10126Padding");
    cipher.init(Cipher.DECRYPT_MODE, keySpec, ivSpec);
    byte[] plainBMP = cipher.doFinal(cipherBMP);
    Files.write(Paths.get("plain1.bmp"), plainBMP);
  }

  static void P2() throws Exception {
    byte[] cipher = Files.readAllBytes(Paths.get("cipher2.bin"));
    byte[] shuffledCipher = shuffleBlocks(cipher, 16);
    byte[] key = generateKey();
    byte[] iv = new byte[16];

    SecretKeySpec secretKey = new SecretKeySpec(key, "AES");
    IvParameterSpec ivSpec = new IvParameterSpec(iv);

    Cipher cipherInst = Cipher.getInstance("AES/CBC/NoPadding");
    cipherInst.init(Cipher.DECRYPT_MODE, secretKey, ivSpec);

    byte[] plain = cipherInst.doFinal(shuffledCipher);
    Files.write(Paths.get("plain2.txt"), plain);
  }

  static void P3() throws Exception {
    byte[] cipherBMP = Files.readAllBytes(Paths.get("cipher3.bmp"));
    byte[] otherBMP = Files.readAllBytes(Paths.get("plain1.bmp"));

    byte[] modifiedBMP = cipherBMP;
    int headerSize = 3000;
    System.arraycopy(otherBMP, 0, modifiedBMP, 0, headerSize);

    Files.write(Paths.get("cipher3_modified.bmp"), modifiedBMP);
  }

  static void P4() throws Exception {
    byte[] plainA = Files.readAllBytes(Paths.get("plain4A.txt"));
    byte[] cipherA = Files.readAllBytes(Paths.get("cipher4A.bin"));
    byte[] cipherB = Files.readAllBytes(Paths.get("cipher4B.bin"));

    byte[] plainB = cipherB;
    int length = Math.min(plainA.length, cipherA.length);
    length = Math.min(length, cipherB.length);
    for (int i = 0; i < length; i++) {
      plainB[i] = (byte) (cipherB[i] ^ cipherA[i] ^ plainA[i]);
    }

    Files.write(Paths.get("plain4B.txt"), plainB);
  }

  static void P5() throws Exception {
    byte[] cipherBMP = Files.readAllBytes(Paths.get("cipher5.bmp"));

    byte[] plainBMP;
    byte[] iv = new byte[16];
    byte[] key = new byte[16];
    IvParameterSpec ivSpec = new IvParameterSpec(iv);
    byte[] knownHeader = new byte[] { 66, 77 };

    for (int i = 0; i < 100; i++) {
      for (int j = 1; j <= 12; j++) {
        for (int k = 1; k <= 31; k++) {
          key[0] = (byte) (i);
          key[1] = (byte) (j);
          key[2] = (byte) (k);
          SecretKeySpec keySpec = new SecretKeySpec(key, "AES");
          Cipher cipher = Cipher.getInstance("AES/CBC/ISO10126Padding");

          cipher.init(cipher.DECRYPT_MODE, keySpec, ivSpec);
          try {
            plainBMP = cipher.doFinal(cipherBMP);

            if (Arrays.equals(Arrays.copyOfRange(plainBMP, 0, knownHeader.length), knownHeader)) {
              Files.write(Paths.get("plain5.bmp"), plainBMP);
              return;
            }
          } catch (BadPaddingException e) {
            System.err.println(e);
          }
        }
      }
    }
  }

  public static void main(String[] args) {
    try {
      P1();
      P2();
      P3();
      P4();
      P5();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}
