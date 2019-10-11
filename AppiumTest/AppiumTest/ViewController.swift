//
//  ViewController.swift
//  AppiumTest
//
//  Created by Andres Lopez on 10/11/19.
//  Copyright © 2019 Bolted, LLC. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var theLabel: UILabel!
    var pressCount: Int = 0

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }

    @IBAction func buttonPressed(_ sender: Any) {
        pressCount += 1
        theLabel.text = "Button press count: \(pressCount)"
    }

}
