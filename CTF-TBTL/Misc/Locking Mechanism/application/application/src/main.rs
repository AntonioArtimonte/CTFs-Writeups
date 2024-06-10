use std::io;
use std::sync::{Arc, Mutex, Condvar};
use std::thread;
use std::time::{Duration, Instant};

struct ThreadMeta {
    input: Vec<usize>,
    output: usize,
    code: u32,
}

impl ThreadMeta {
    fn new(input: Vec<usize>, output: usize, code: u32) -> Self {
        ThreadMeta { input, output, code }
    }
}

fn create_thread(
    input: Vec<usize>,
    output: usize,
    code: u32,
    locks: Arc<Vec<Arc<(Mutex<bool>, Condvar)>>>,
    key: Arc<Mutex<Vec<Vec<u8>>>>,
) -> impl FnOnce() + Send + 'static {
    move || {
        println!("Thread {}: Trying to unlock with code {}", output, code);

        // Attempt to acquire each necessary input lock
        for &i in &input {
            let (lock, cvar) = &*locks[i];
            let mut guard = lock.lock().unwrap();
            let start = Instant::now();
            while !*guard {
                if cvar.wait_timeout(guard, Duration::from_secs(10)).unwrap().1.timed_out() {
                    println!("Thread {}: Timeout while waiting for lock {}", output, i);
                    return; // Optionally return error or handle timeout case
                }
                guard = cvar.wait(guard).unwrap();
            }
        }

        // Critical section: modify the shared resource
        let (out_lock, out_cvar) = &*locks[output];
        {
            let mut out_guard = out_lock.lock().unwrap();
            *out_guard = true;
            out_cvar.notify_all();
        }

        // Update shared key structure
        let mut key_guard = key.lock().unwrap();
        let index = (code % 9) as usize;
        key_guard[index].push((code / 9).try_into().unwrap());
        println!("Thread {}: Unlock done {}", output, code);
    }
}

fn main() {
    println!("Enter indices separated by commas (e.g., 1,2,3):");
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let config_input: Vec<usize> = input.trim().split(',')
        .map(|s| s.trim().parse().expect("Please enter valid integers separated by commas"))
        .collect();

    let num_threads = 104; // Adjust based on your configuration
    let arcs = Arc::new((0..num_threads).map(|_| Arc::new((Mutex::new(false), Condvar::new()))).collect::<Vec<_>>());
    let key_entropy = Arc::new(Mutex::new(vec![vec![]; 9]));

    let key_config = vec![
        (vec![31], 1924),
        (vec![11], 133),
        (vec![45, 37], 1319),
        (vec![86, 0], 2005),
        (vec![1, 91], 1025),
        (vec![40], 1372),
        (vec![76], 7),
        (vec![102, 50], 755),
        (vec![46, 84], 2050),
        (vec![56, 2], 1332),
        (vec![88, 26], 124),
        (vec![6], 1213),
        (vec![27], 1559),
        (vec![2, 56], 1940),
        (vec![35], 2225),
        (vec![44, 25], 645),
        (vec![15, 23], 2302),
        (vec![34], 489),
        (vec![77, 42], 857),
        (vec![94], 1303),
        (vec![42, 96], 1608),
        (vec![25, 64], 1485),
        (vec![61, 54], 20),
        (vec![64, 25], 2293),
        (vec![28, 29], 826),
        (vec![13, 72], 1573),
        (vec![67], 252),
        (vec![57], 1420),
        (vec![100, 52], 2257),
        (vec![100, 52], 1880),
        (vec![99, 29], 1743),
        (vec![70, 7], 1420),
        (vec![68, 63], 475),
        (vec![26, 88], 1460),
        (vec![48, 3], 1798),
        (vec![66], 2131),
        (vec![19], 2018),
        (vec![82], 1366),
        (vec![47, 4], 225),
        (vec![16], 2032),
        (vec![10, 33], 1582),
        (vec![91, 1], 1321),
        (vec![80, 49], 1249),
        (vec![12, 75], 1951),
        (vec![13, 72], 1269),
        (vec![82], 1117),
        (vec![34], 1582),
        (vec![91, 1], 1810),
        (vec![86, 0], 146),
        (vec![24, 30], 1202),
        (vec![35], 1854),
        (vec![16], 1728),
        (vec![39, 59], 961),
        (vec![4, 41], 1066),
        (vec![12, 87], 465),
        (vec![93, 60], 817),
        (vec![37, 45], 1465),
        (vec![5, 85], 1582),
        (vec![63, 68], 2106),
        (vec![16], 1577),
        (vec![22, 92], 1858),
        (vec![12, 87], 1839),
        (vec![47, 41], 1618),
        (vec![97, 101], 429),
        (vec![72, 13], 409),
        (vec![59, 51], 1768),
        (vec![36, 71], 1447),
        (vec![32, 90], 709),
        (vec![97, 101], 1789),
        (vec![50, 102], 1273),
        (vec![102, 14], 2212),
        (vec![19], 124),
        (vec![56, 2], 1177),
        (vec![54, 43], 1078),
        (vec![0, 86], 1567),
        (vec![27], 1825),
        (vec![79, 55], 322),
        (vec![49, 80], 1153),
        (vec![67], 1063),
        (vec![60, 93], 1187),
        (vec![30, 24], 358),
        (vec![95, 18], 560),
        (vec![], 1663),
        (vec![84, 46], 1217),
        (vec![34], 1049),
        (vec![40], 1141),
        (vec![31], 1826),
        (vec![27], 150),
        (vec![67], 124),
        (vec![95, 20], 601),
        (vec![68, 63], 282),
        (vec![11], 1448),
        (vec![43, 61], 2053),
        (vec![73, 92], 1573),
        (vec![62, 38], 2104),
        (vec![42, 77], 466),
        (vec![80, 49], 598),
        (vec![89, 98], 1402),
        (vec![95, 20], 1787),
        (vec![65, 100], 591),
        (vec![39, 59], 336),
        (vec![98, 81], 1998),
        (vec![35], 1087),
        (vec![82], 990),
    ];

    let threads_meta = config_input.into_iter().map(|i| {
        let (input, code) = &key_config[i];
        ThreadMeta::new(input.clone(), i, *code)
    }).collect::<Vec<_>>();

    let mut handles = vec![];
    for meta in threads_meta {
        let locks_clone = Arc::clone(&arcs);
        let key_clone = Arc::clone(&key_entropy);
        handles.push(thread::spawn(move || {
            let thread_func = create_thread(meta.input, meta.output, meta.code, locks_clone, key_clone);
            thread_func();
        }));
    }

    for handle in handles {
        let _ = handle.join().expect("Thread failed");
    }

    // Decrypt the flag
    let key = key_entropy.lock().unwrap();
    let flag = vec![
        236, 213, 246, 206, 213, 171, 145, 141, 90, 153, 48, 22, 228, 116, 29, 247, 246, 87, 5, 82,
        122, 158, 10, 231, 194, 190, 144, 5, 157, 110, 71, 83, 217, 109, 211, 221, 182, 242, 62,
        255, 152, 72, 133, 194, 162, 238, 181, 228, 158,
    ];

    println!("aaa");

    let decrypted_flag = key.iter()
    .flat_map(|segment| segment.iter())
    .zip(flag.iter())
    .map(|(k, f)| k ^ f)
    .collect::<Vec<u8>>();

    let result = String::from_utf8(decrypted_flag).expect("Failed to convert decrypted bytes to string");
    println!("Decrypted Flag: {}", result);

    println!("Decrypted Flag:");
    for (i, byte) in flag.iter().enumerate() {
        print!("{}", byte ^ key[i % key.len()][0]);
    }
    println!();
}
