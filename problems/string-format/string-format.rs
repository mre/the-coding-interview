fn format_manual(orig_str: &str, args: Vec<&str>) -> String {
    let mut new_str = orig_str.to_string();

    for (i, arg) in args.iter().enumerate() {
        let temp_str = new_str.clone();
        let parts: Vec<&str> = temp_str
            .split(format!("{}{}{}", "{", i.to_string(), "}").as_str())
            .collect();

        new_str = parts.join(arg);
    }

    new_str
}

fn main() {
    println!("{}\n", format_manual("Hello {0} {1}", vec!["Mr.", "X"]));

    println!("{}\n", format!("Hello {0} {1}", "Mr.", "X"));
}
